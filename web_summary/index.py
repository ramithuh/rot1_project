import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

#import package
import plotly.io as pio
pio.templates.default = "plotly"

# Start streamlit app
st.sidebar.title('SELEX Data Overview/Explorer')
st.markdown(
    """
    <style>
    [data-testid="stSidebarContent"] {
        width: 550px !important;
    }
    [data-testid="stSidebar"] {
        width: 550px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# List out files in SELEX directory
gz_files = sorted([x for x in os.listdir("/home/ruh/SELEX_Cluster") if ('.gz' in x)])
file_names = sorted([x for x in os.listdir("/home/ruh/SELEX_Cluster") if ('.gz' in x and "ZeroCycle" not in x)])

# Quick summary
with st.sidebar.expander("File structure:", expanded=True):
    st.write(f"**Rounds 1-4 File Count:** {len(file_names)} *(eg. Alx4_ESP_TGGTAG20NCG_1.txt.gz)*")
    st.write(f"**ZeroCycle Count:** {len(gz_files) - len(file_names)} *(eg. ZeroCycle_ES0_TGGTAG20NCG_0.txt.gz)*")

    code1 = '''$ find . -name "*.gz" | grep -v "ZeroCycle" | wc -l 
2069'''
    code2 = '''$ find . -name "*.gz" | grep "ZeroCycle" | wc -l
441'''
    code3 = '''total_lines=0; for file in "T"_*4.txt.gz; do [ -f "$file" ] && echo $file && lines=$(zcat "$file" | wc -l) && total_lines=$((total_lines + lines)); done; echo "Total DNA Fragments: $((total_lines / 4))"
T_ESW_TGGGCG20NCGT_4.txt.gz
Total DNA Fragments: 2103222'''
    st.code(code1, language="bash")
    st.code(code2, language="bash")
    st.write(f"Get total DNA count for specified protein in round 4 (e.g. T)")
    st.code(code3, language="bash")



## Plot data 

# Read the CSV file
df = pd.read_csv('summary.csv')

# Get all numeric columns
numeric_columns = ['all_count', 'valid_count', 'total_unique_count', 'intersection_count']

# Create a dropdown to select the sorting column
sort_column = st.selectbox(
    "Sort proteins by:",
    options=numeric_columns + ['protein_id'],
    index=0
)

# Create a multi-select to choose which columns to display
display_columns = st.multiselect(
    "Select columns to display:",
    options=numeric_columns,
    default=numeric_columns[:2]  # Default to first two numeric columns
)

# Sort the data
sorted_data = df.sort_values(by=sort_column, ascending=False)

# Create the bar chart
fig = px.bar(
    sorted_data, 
    x='protein_id', 
    y=display_columns,
    title='Distribution of Protein Data',
    labels={'value': 'Count', 'variable': 'Data Type', 'protein_id': 'Protein'},
    height=600,
    barmode='group'  # Change this from 'stack' to 'group'
)

# Update layout
fig.update_layout(
    xaxis_title="Protein",
    yaxis_title="Count",
    xaxis_tickangle=-90,
    bargap=0.2
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)

# Display the sorted data
st.write("Sorted Protein Data:")
st.dataframe(sorted_data)

# Save the figure as an HTML file
fig.write_html("protein_data_visualization.html")