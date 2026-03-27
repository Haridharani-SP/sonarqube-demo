import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Basic Dashboard", layout="wide")

# Title
st.title("📊 Simple Streamlit Dashboard")

# Sidebar
st.sidebar.header("Settings")
num_rows = st.sidebar.slider("Select number of rows", 10, 100, 50)

# Generate sample data
data = pd.DataFrame({
    "Category": np.random.choice(["A", "B", "C"], num_rows),
    "Values": np.random.randn(num_rows)
})

# Layout
col1, col2 = st.columns(2)

# Column 1 - Table
with col1:
    st.subheader("📋 Data Table")
    st.dataframe(data)

# Column 2 - Chart
with col2:
    st.subheader("📈 Value Distribution")
    st.bar_chart(data["Values"])

# Metrics
st.subheader("📌 Summary")
col3, col4, col5 = st.columns(3)

col3.metric("Total Rows", len(data))
col4.metric("Average Value", round(data["Values"].mean(), 2))
col5.metric("Max Value", round(data["Values"].max(), 2))

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
