import streamlit as st
import pandas as pd
import numpy as np

#Title of application
st.title("Hello streamlit")

#Display text
st.write("This is a simple text")

#Create and display a Dataframe
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

st.write("Here is the dataframe")
st.write(df)

#Display a line chart
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)