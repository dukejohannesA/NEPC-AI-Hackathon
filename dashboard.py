import streamlit as st
import pandas as pd
import plotly.express as px

st.title("NEPC Media Analytics Dashboard")

# Fake readership data
data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "print_readers": [3200, 2800, 3100, 2900, 3400, 4100, 3800],
    "online_readers": [8500, 9200, 8800, 9600, 10200, 7800, 6900]
}

df = pd.DataFrame(data)

st.subheader("Weekly Readership")
fig = px.line(df, x="day", y=["print_readers", "online_readers"],
              title="Print vs Online Readers",
              labels={"value": "Readers", "variable": "Platform"})
st.plotly_chart(fig)

st.subheader("Raw Data")
st.dataframe(df)