#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('dir')


# In[6]:


# Importing pandas library

import pandas as pd


# In[7]:


# Read the excel file

excelFile = pd.ExcelFile('Input File.xlsx')


# In[9]:


excelFile


# In[12]:


for i in range(1,11):
    excelFile.parse(f"Sheet{i}").to_csv(f"CSV Sheet {i}.csv")
    print (i)

