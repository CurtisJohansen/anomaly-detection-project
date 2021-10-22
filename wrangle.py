####### Imports #######

import pandas as pd
import numpy as np
import os
from sklearn.impute import SimpleImputer
from env import host, user, password

####### Curriculum Log Data #######

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    
def new_logs_df():
    '''
    This function reads the data from the Codeup db into a df and returns the df.
    '''
    # Create SQL query
    
    sql_query = """
    select *
    from logs as l
    left join cohorts as c on l.cohort_id = c.id;
    """
    # Read in DataFrame from Codeup db
    
    df = pd.read_sql(sql_query, get_connection('curriculum_logs'))
    
    return df    

    
def get_logs_df():
    '''
    This function reads in data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('access_logs.csv'):
        
        # If csv file exists, read in data from csv file
        
        df = pd.read_csv('access_logs.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        
        df = new_logs_df()
        
        # Write DataFrame to a csv file
        
        df.to_csv('access_logs.csv')
        
    return df


def prep_logs(df):
    '''
    prep_logs will take in the curriculum log data and prepare it for use by 
    setting date to the index, and converting it to datetime format,
    changing start date and end date to datetime format,
    renaming columns for easier use, drop unecessary columns, create new features,
    create objectified columns for easier read, and drops duplicates
    '''
    # drop 'deleted_at' column because no entries have a value
    
    df = df.drop(columns=['deleted_at'])

    # drop columns with null entries
    
    df = df.dropna()

    # combine date and time columns into one date-time column to use for indexing
    
    df = df.set_index(pd.to_datetime(df.date + ' ' + df.time))

    # make 'time' column a date/time type
    
    df.time = pd.to_datetime(df.time)
    df.date = pd.to_datetime(df.date)
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)
    df.created_at = pd.to_datetime(df.created_at)
    df.updated_at = pd.to_datetime(df.updated_at)
    
    # create accessed_after column - references if user accessed materials after graduation date at the time of query
    
    df['accessed_after'] = df.index > df.end_date
    
    # turn accessed_after to integers instead of booleans
    
    df['accessed_after'] = df['accessed_after'].astype(int)
    
    # create program_name column
    df['program_name'] = 0
    
    #program_id of 1 is Full Stack PHP
    
    df['program_name'] = np.where(df['program_id']==1, 'Web Dev - Front End', 0)
    
    #program_id of 2 is Web Development
    
    df['program_name'] = np.where(df['program_id']==2, 'Web Dev - Java', df['program_name'])
    
    #program_id of 3 is Data Science
    
    df['program_name'] = np.where(df['program_id']==3, 'Data Science', df['program_name'])
    
    #program_id of 4 is Front End
    
    df['program_name'] = np.where(df['program_id']==4, 'Web Dev - Front End', df['program_name'])

    return df  