
#Importing Libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components


# basic settings 
st.set_page_config(layout="wide")
st.title("McGonagall's Army")
st.text('Data analysis from the Goodreads starting from the year 2000')
st.write('''***''')
st.write('''
Our boss wants to publish new book and she wants to be in best books on goodread. We will guide her with analysing books of data from good read.But first lets look at what is our approach;
Publishing a book in a world where media is consumed at less than 30 second chunks can be bit of a gamble!!But with mountains of data at our disposal it is possible to weigh the odds in our favour if we know how to read it the right way.
''')

# sidebar 
st.sidebar.markdown('<i class="material-icons"></i>', unsafe_allow_html=True)
st.sidebar.markdown('<i class="material-icons"></i>', unsafe_allow_html=True)
st.sidebar.markdown("## Our LinkedIn Profiles")
link = '[Shahid Qureshi](https://www.linkedin.com/in/shahid-qureshi-8190/)'
link2 = '[Dilan Udawala](http://github.com)'
link3 = '[Hedaya Ali](http://github.com)'
link4 = '[Umut Aktas](https://linkedin.com/aktumut)'

st.sidebar.markdown(link, unsafe_allow_html=True)
st.sidebar.markdown(link2, unsafe_allow_html=True)
st.sidebar.markdown(link3, unsafe_allow_html=True)
st.sidebar.markdown(link4, unsafe_allow_html=True)

# Importing Data
def importing_data():
    df=pd.read_csv("big_books_clean.csv")
    return df
df=importing_data()

# print head
st.subheader('Head')
st.dataframe(df.head())

# print head
st.subheader('Data description')
st.dataframe(df.describe())

# select columns widget
cols = ["Title", "URL", "Author",  "Rating", "Reviews", "Pages", "Year", "Series", "Setting", "Awards", "Genres"]
st_ms = st.multiselect("Columns", df.columns.tolist(), default=cols)

# display dataframe
st.subheader('DataFrame')
st.dataframe(df)

# Year vs Average_rating 
st.subheader('Highest average rating by year')
st.table(df.groupby("Year").Average_rating.mean().reset_index()\
.round(2).sort_values("Average_rating", ascending=False)\
.assign(average_rating=lambda x: x.pop("Average_rating").apply(lambda y: "%.2f" % y)))

# # Page slider
# values = st.sidebar.slider("Pages", float(df.Pages.min()), 1000., (50., 300.))
# f = px.histogram(df.query(f"Pages.between{values}"), x="Pages", nbins=15, title="Price distribution")
# f.update_xaxes(title="Pages")
# f.update_yaxes(title="Count")
# st.plotly_chart(f)

# display minmax average
HtmlFile = open('components/temp-plot.html', 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height=600)

# display corelations
HtmlFile = open('components/plot_with_with_corelations.html', 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height=600)

# display genres
HtmlFile = open('components/Genres_years.html', 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height=600)

# best books
HtmlFile = open('components/Best_books_2006.html', 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height=600)

# display line chart 
st.subheader('Averages vs Years')
st.line_chart(df)

# display area chart 
st.subheader('Ratings vs pages')
st.area_chart(df)


#Filling numerical data of Number of Ratings
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
#Filling numerical data of Number of Reviews
df['Reviews'] = df['Reviews'].fillna(df['Reviews'].mean())
#Filling numerical data of Average Ratings
df['Average_rating'] = df['Average_rating'].fillna(df['Average_rating'].mean())
#Filling numerical data of Number of Pages
df['Pages'] = df['Pages'].fillna(df['Pages'].mean())



#Filling categorical data of Published Year
df['Year'] = df['Year'].fillna(df['Year'].mode()[0])
#Filling categorical data of Series
df['Series'] = df['Series'].fillna(df['Series'].mode()[0])
#Filling categorical data of Genres
df['Genres'] = df['Genres'].fillna(df['Genres'].mode()[0])
#Filling categorical data of Places
df['Setting'] = df['Setting'].fillna(df['Setting'].mode()[0])


