import streamlit as st
import pandas as pd
import duckdb

data = {"a" : [1,2,3], "b" : [4,5,6]}
df = pd.DataFrame(data)

st.title("Table1")
sql_query = st.text_area(label = "tape your input")
st.write(f"{sql_query}")
if sql_query :
    result = duckdb.query(sql_query).df()
    st.dataframe(result)
else :
    st.write("No result")


