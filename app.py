import pandas as pd
import streamlit as st
data = pd.read_csv('test_csv.csv')
st.dataframe(data, width=10, height=5)
