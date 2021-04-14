#!/usr/bin/env python
# coding: utf-8

# ## Data Preparation
# 1. Importing Libraries and Data Set
# 2. Understanding Data Set
# 3. Cleaning Data Set

# ### 1.Importing Libraries and Data Set

# In[18]:


#Importing Libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import streamlit as st

# basic settings 
st.set_page_config(layout="wide")
st.title("McGonagall's Army")
st.text('Minerva McGonagall was born on 4 October to Robert McGonagall, a Muggle Presbyterian minister, and his wife Isobel Ross, a witch. She was the couple\'s first child and was named after her mother\'s grandmother, a very powerful witch. By then, her parents lived on the outskirts of Caithness in the Scottish Highlands, in a village where mostly Muggles lived.')

#Importing Data
def importing_data():
    df=pd.read_csv("test_csv.csv")
    return df
df=importing_data()

# display dataframe
st.dataframe(df)

# display line chart 
st.line_chart(df)

df.head()

df.info()


# We have 12 different columns which can be categorical or numerical data in our data set. Also, we can say that there are some non-values that we should take care of! Let's check how big they are.

# In[27]:


#Heat map of null cells
def plotting_null_data():
    fig = plt.figure(figsize=(15,5))
    fig.add_subplot(121)
    plt.title('Nulls of Data')
    sns.heatmap(df.isnull(), cmap='plasma')
    return plt.show()
plotting_null_data()


# In[28]:


print("Percentage of Null Values")
missing_percentage = df.isnull().sum() * 100 / len(df) #Calculating percentage of missing values
missing_percentage


# We have pretty less null value in our data set. Only "Places" have 32% null value.
# 
# Lets look at **basic statistical information** of our data set.

# In[29]:


df.describe()


# Here is the results;
# * The mean value and maximum and minimum values of the **Number of Ratings** differences are too big! That means we should **normalize** this column.
# * The mean value and maximum and minimum values of the **Number of Reviews** differences are too big! That means we should **normalize** this column.
# * The mean value and maximum and minimum values of the **Average Ratings** differences are too close! That means we should **scale** this column, for better visualizing and understanding the distributions.
# * The mean value and maximum and minimum values of the **Number of Pages** differences are too big! That means we should **normalize** this column.
# * We can count **Year** and **Series** columns as **categorical** data. 
# 

# ### 2.Cleaning Data Set

# #### Filling the null data 
# There are a lot of approaches for filling the data.
# * For filling numerical data we will use mean values 
# * For filling categorical data we will use mode values
# 
# **Filling numerical data**
# 

# In[44]:


#Filling numerical data of Number of Ratings
df['Number of Ratings'] = df['Number of Ratings'].fillna(df['Number of Ratings'].mean())
#Filling numerical data of Number of Reviews
df['Number of Reviews'] = df['Number of Reviews'].fillna(df['Number of Reviews'].mean())
#Filling numerical data of Average Ratings
df['Average Ratings'] = df['Average Ratings'].fillna(df['Average Ratings'].mean())
#Filling numerical data of Number of Pages
df['Number of Pages'] = df['Number of Pages'].fillna(df['Number of Pages'].mean())


# **Filling categorical data**

# In[45]:


#Filling categorical data of Published Year
df['Published Year'] = df['Published Year'].fillna(df['Published Year'].mode()[0])
#Filling categorical data of Series
df['Series'] = df['Series'].fillna(df['Series'].mode()[0])
#Filling categorical data of Genres
df['Genres'] = df['Genres'].fillna(df['Genres'].mode()[0])
#Filling categorical data of Places
df['Places'] = df['Places'].fillna(df['Places'].mode()[0])


# Lets look at last status of data set

# In[46]:


print("Percentage of Updated Null Values")
missing_percentage_updated = df.isnull().sum() * 100 / len(df) #Calculating percentage of missing values
missing_percentage_updated


# Now we don't have any missing values!
# 
# 

# ## Data Visualization
# 1. Correlation Maps
# 2. Data Distributions
# 3. Interesting Informations
# 4. Graphs with Places

# ### 1.Correlation Maps

# ### 2.Data Distributions

# ### 3.Interesting Informations

# ### 4.Graphs with Places

# 

# In[ ]:





# 

# <a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=a0867bd3-5624-476b-af8a-bd1f917bd510' target="_blank">
# <img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
# Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
