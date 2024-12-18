import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
def load_data():
    return pd.read_csv("student csv.csv")

data = load_data()

# Streamlit App
st.title("Student Performance Analysis")

# Sidebar Filters
st.sidebar.header("Filters")

gender = st.sidebar.selectbox("Select Gender", ["All"] + data['Gender'].unique().tolist())
school_type = st.sidebar.selectbox("Select School Type", ["All"] + data['School_Type'].unique().tolist())

# Filter data
data_filtered = data.copy()
if gender != "All":
    data_filtered = data_filtered[data_filtered['Gender'] == gender]
if school_type != "All":
    data_filtered = data_filtered[data_filtered['School_Type'] == school_type]

# Display filtered data
st.subheader("Filtered Data")
st.write(data_filtered)

# Descriptive Statistics
st.subheader("Descriptive Statistics")
st.write(data_filtered.describe(include='all'))

# Visualization
st.subheader("Visualizations")



# Scatterplot
x_col = st.selectbox("Select X-axis for Scatterplot", data_filtered.columns)
y_col = st.selectbox("Select Y-axis for Scatterplot", data_filtered.columns)

if x_col and y_col:
    plt.figure(figsize=(8, 5))
    genders = data_filtered['Gender'].unique()
    colors = ['blue', 'orange']  # Define colors for genders
    for i, gender in enumerate(genders):
        gender_data = data_filtered[data_filtered['Gender'] == gender]
        plt.scatter(gender_data[x_col], gender_data[y_col], label=gender, color=colors[i % len(colors)], alpha=0.7)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{x_col} vs {y_col}")
    plt.legend(title="Gender")
    st.pyplot(plt)

# Predictive Tool Placeholder
st.subheader("Predictive Tool (Currently working on it)")
st.write("This feature will allow users to predict exam scores based on input factors.")

st.write("\n\n---")
st.write("Developed with ❤️ by falansh.")

