# Incubyte-assessment

## Overview:
This repository contains implementation of given assessment. The working of data pipeline is demonstarted using tools listed below:-

 **Concepts:**
- Data processing
- ETL

**Tools & Technologies:**
- Jupyter Notebook
- MySQL Workbench
- XAMPP Server
- Pandas
- Conda Environment
- MySQL connector
## Working:
- Firstly MySQL database has been created with specified schema.
- [```Submission.ipynb```] python script, fetches database by establishing connection with MySQL server. and Make sure the XAMMP server is running while executing the script
- The retrieved data is fitted into pandas dataframe for further table manipulation.
- ```show_data()``` & ```getfile()``` functions are called to fetch the desired data rows and generating ```.csv``` and ```string``` file formats to specified path, accepting country names as parameters for filtering rows. 
- For example: ```get_file("IND")``` generates [```IND.csv```] to the specified local path. To see sample output files go into Table and then output.





