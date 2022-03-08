#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('dir')


# In[42]:


# Importing pandas and seaborn library

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[16]:


df = pd.read_csv("gapminder-FiveYearData.csv")


# In[17]:


df.head()


# In[18]:


df.shape


# In[31]:


pivotTable = pd.pivot_table(data=df,index=['year'],columns=['country'],values=['lifeExp'])


# In[32]:


pivotTable


# In[52]:


plt.figure(figsize=(15,15))
sns.heatmap(pivotTable, cmap='RdYlGn')
plt.savefig('Heat Map')


# In[ ]:




