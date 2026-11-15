import pandas as pd
import streamlit as st
import altair as alt

sales = st.read_csv(r'C:\Users\Shivani\Downloads\TVsales.csv')

st.title("TV Sales Impact Analysis")
dataset=st.checkbox("View the TV sales Dataset")
if dataset:
    st.dataframe(sales)
sel=st.radio('Select an item for the sales comparison analysis:',['Income','Price','CompPrice'])
fig=alt.Chart(sales).mark_circle().encode(
    x='Sales',y=sel,size=sel).properties(width=650,height=450)
st.altair_chart(fig,use_container_width=True)