#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


import os


# In[9]:


os.getcwd()


# In[10]:


os.chdir("G:\Python Scripts")


# In[11]:


data=pd.read_excel("Data analytics.xlsx")


# In[12]:


type(data)


# In[13]:


data


# In[16]:


data.head()


# In[17]:


data.tail()


# In[20]:


data.columns


# In[21]:


data['Favorite Book']


# In[23]:


data.isnull().any()


# In[24]:


data.isnull().sum()


# In[25]:


data.dropna(axis=1)


# In[26]:


data


# In[27]:


newdata=data.dropna(axis=1)


# In[28]:


newdata


# In[32]:


newdata.dtypes


# In[33]:


newdata.info()


# In[34]:



newdata.describe()


# In[36]:


#no numeric value to plot
newdata.plot()


# In[42]:


newdata[['Age Group','Preferred Book Genre']]


# In[61]:


#convert data frame into categorical data
pd.get_dummies(newdata)


# In[65]:


nd=pd.get_dummies(newdata)


# In[68]:


#bar graph(something unexpected)
nd.plot(kind='bar')


# In[69]:


#not working?
# newdata.Age Group=pd.Categorical(newdata.Age Group,['Below 14','14-22','22-44','44-60','60 above'],ordered=True)


# In[72]:


nd1=newdata[['Age Group','Preferred Book Genre']]


# In[75]:


pd.get_dummies(nd1).plot(kind='bar')


# In[81]:


nd2=newdata[['Gender','Preferred Book Genre']]


# In[82]:


pd.get_dummies(nd2).plot(kind='bar')


# In[ ]:


#maybe correlation needs data science

