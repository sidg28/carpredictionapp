import numpy as np
import pandas as pd
import streamlit as st
def app(cars_df):
    # Displaying orginal dataset
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.expander("View Dataset"):
        st.table(cars_df)

    # Display descriptive statistics.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(cars_df.describe())    
    
    # ADD NEW CODE FROM HERE
    beta_1,beta_2,beta_3 = st.columns(3)
    with beta_1:
      if st.checkbox('Show all column names'):
        st.table(list(cars_df.columns))
    with beta_2:
      if st.checkbox('View column data types'):
        st.table(list(cars_df.dtypes))
    with beta_3:
      if st.checkbox('View column data'):
        column_data = st.selectbox('Select column',tuple(cars_df.columns))
        st.write(cars_df[column_data])