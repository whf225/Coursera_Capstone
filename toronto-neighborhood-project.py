#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import libraries
import numpy as np # library to handle data in a vectorized manner
import pandas as pd # library for data analsysis


# In[4]:


# download the original data
url='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

df=pd.read_html(url, header=0)[0]

df.head()


# In[29]:


#drop the not assigned cell

df1 = df[ ~ df['Borough'].str.contains('Not assigned') ]  

df1.head()


# In[30]:


# split the data
df2 = df1.drop('Neighborhood', axis=1).join(df1['Neighborhood'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('Neighborhood'))
df2.head()


# In[33]:


# joint the data
def ab(df2):
    return','.join(df2.values)
    

df2 = df2.groupby(['Postal code','Borough'])['Neighborhood'].apply(ab)
df2 = df2.reset_index()
df2.head()


# # there are 4 steps for me to prepare the dataframe
#  ## 1.download the original data
#  ## 2.delete the row that 'borough' is not assigned
#  ## 3.seperate the data to make sure every row contains only 1 neighborhood
#  ## 4.combine the data and use the','split every neighborhood

# In[34]:


df2.shape


# In[43]:


df_gd = pd.read_csv("http://cocl.us/Geospatial_data")  
df_gd.head()


# In[49]:


#change column name
df_gd.rename(columns={'Postal Code':'Postal code'},inplace = True)
df_gd.head()


# In[52]:


df_gd_final = pd.merge(df2,df_gd,on='Postal code')
df_gd_final.head()


# In[ ]:




