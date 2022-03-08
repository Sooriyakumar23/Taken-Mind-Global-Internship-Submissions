#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Installing sklearn library(Machine Learning library which consists of famous algorithms)

get_ipython().system('pip install sklearn')


# In[2]:


# Importing necessary libraries

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# In[3]:


get_ipython().system('dir')


# In[4]:


# Importing Iris.csv data file to a DataFrame

iris = pd.read_csv('Iris.csv')


# In[5]:


# Shape

iris.shape


# In[6]:


# Describe

iris.describe()


# In[7]:


# Number of null values

iris.isnull().sum()


# No null values at any feature. Therefore, no need to fill or remove null values

# In[8]:


# First 5 data points

iris.head()


# In[9]:


# Separate dataset into 2 pieces
    # 1. Features -----> X
    # 2. Label    -----> Y

X = iris[iris.columns[1:-1]]
y = iris["Species"]


# In[10]:


# First 5 data points in features / X

X.head()


# In[11]:


# Shape of X

X.shape


# In[12]:


# First 5 data points in label / y

y.head()


# In[13]:


# Shape of y

y.shape


# In[14]:


# Labels and their counts

y.value_counts()


# It is a balanced dataset

# In[15]:


# 70% train set & 30% test set split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[16]:


# Shapes of each 4 data

print ("Training features shape is", X_train.shape)
print ("Testing features shape is", X_test.shape)
print ("Training label shape is", y_train.shape)
print ("Testing label shape is", y_test.shape)


# In[17]:


# Initializing decision tree classifier algorithm as an object

clf = DecisionTreeClassifier(random_state=0)


# In[18]:


# Train the train set (X_train & y_train) on the decision tree classifier object

clf.fit(X_train, y_train)


# In[19]:


# predicting result for train input

predict_train = clf.predict(X_train)


# In[20]:


# predicting result for test input

predict_test = clf.predict(X_test)


# In[21]:


# Accuracies of train and test sets.....

print ("Train set accuracy is", str(accuracy_score(y_train, predict_train) * 100) + "%")

print ("Test set accuracy is", str(accuracy_score(y_test, predict_test) * 100) + "%")

