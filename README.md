# Anomaly Detection Project


### Description

Look at the data in order to find trends and abnormalities in the Codeup Curriculum Access Log.

### Deliverables

Create a notebook for review, a single slide to document our finds similar to an executive summary and reply to the email with our discoveries.

### Project Questions

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
3. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
4. Which lessons are least accessed? 
5. What topics are grads continuing to reference after graduation and into their jobs (for each program)?

### Findings

There are 4 different programs available in the dataset:
    - PHP Full Stack (Web Development)
    - Java Full Stack (Web Development)
    - Data Science
    - Front End (Web Development)

There seems to be some suspicious activity going on with one user accessing 272 pages in the curriculum over a short duration.
    - This user also used a few different IP addresses.
    
There were 468 pages in the curriculum which were only accessed once.
    - Some of these pages were found to be lessons while the others were professional development pages.
    
The following lessons were accessed post graduation:
    - Data Science: SQL, Classification Overview, Classification Scaling
    - Full-Stack Java: Javascript-I, HTML-CSS, Spring
    - Front End: Javascript-I, HTML-CSS, Spring
    
### Data Dictionary    

|          Feature               |            Definition               | Datatype |
|--------------------------------|-------------------------------------|:--------:|
|date                            |date of access                       |datetime64|
|time                            |time page was accessed               |datetime64|
|path                            |path of curriculum page              |object    |
|user_id                         |student identification number        |int64     |
|cohort_id                       |cohort identification number         |float64   |
|ip                              |gender of employee - male or female  |object    |   
|id                              |ip address that accessed curriculum  |float64   | 
|name                            |cohort name                          |object    |                       
|slack                           |identification name for messenger    |float64   |
|start_date                      |start date of cohort                 |datetime64|
|end_date                        |end date of cohort                   |datetime64|
|created_at                      |date and time curriculum was created |datetime64|
|updated_at                      |time of record update                |datetime64|
|program_id                      |id number of the program             |float64   |
|accessed_after                  |page accessed after graduation date = 1, page accessed as a current student = 0|int64     |
|program_name                    |name of program                      |object    | 

### Reproduce My Project

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

Download the wrangle.py and the anomaly-detection-project.ipynb file into your directory

Run the individual_project.ipynb notebook    
    