import streamlit as st
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
})

# Show the dataframe as a table
st.table(df)