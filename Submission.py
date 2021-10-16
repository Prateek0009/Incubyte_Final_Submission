#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as c


# In[2]:


import pandas as pd


# In[3]:


connection = c.connect(host= "localhost",user= "root", database = "multi_spe_hospital")


# In[4]:


cursor = connection.cursor()


# In[5]:


query2 = "select * from patients"


# In[6]:


# executing cursor
cursor.execute(query2)


# In[7]:


# fetching tables
table_rows = cursor.fetchall()
print("Total Number of rows in table:", cursor.rowcount)


# In[8]:


df = pd.read_sql('SELECT * FROM patients', con=connection)  # fitting into pandas dataframe
df.set_index(['CUSTOMER_ID'], inplace=True)  # setting default index


# In[9]:


df


# In[10]:


def show_data(country):
    data = df.loc[df['COUNTRY'] == country]
    print(data)


# In[11]:


def get_file(country):
    data = df.loc[df['COUNTRY'] == country]
    file_name = str(country)
    data.to_csv('C:/Users/prate/Table_' + country + ".csv")  # replace path with your desired path
    print("File has been created to the specified path")


# In[12]:


# calling functions

df1= show_data("IND")
get_file("IND")


# In[13]:


show_data("NYC")
get_file("NYC")


# In[14]:


show_data("USA")
get_file("USA")


# In[15]:


show_data("PHIL")
get_file("PHIL")


# In[16]:


show_data("AU")
get_file("AU")

