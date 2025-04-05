import streamlit as st
import pandas as pd
import sqlite3

st.title("🌍 Global Mental Health Trends Dashboard")

conn = sqlite3.connect("../data/mental_health.db")
df = pd.read_sql("SELECT * FROM mental_health", conn)

countries = df['Country'].unique()
selected_country = st.selectbox("Select a Country", countries)

filtered_df = df[df['Country'] == selected_country]
st.line_chart(filtered_df.groupby('Year')['Value'].mean())

st.write("### Raw Data")
st.dataframe(filtered_df)
