import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

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
    st.code(code1, language="bash")
    st.code(code2, language="bash")


# Generate dummy data for 450 proteins
np.random.seed(42)
num_proteins = 10
protein_names = [f'Protein_{i+1}' for i in range(num_proteins)]
count_series = np.arange(1, num_proteins + 1) + 5 # Total count
unique_count_series = np.arange(1, num_proteins + 1)  # Total count

dummy_data = pd.DataFrame({
    'Protein': protein_names,
    'Total Count': count_series,
    'Unique Count': unique_count_series
})

# Sort the data by Binding Frequency in decreasing order
sorted_data = dummy_data.sort_values(by='Total Count', ascending=False)

fig = px.bar(sorted_data, x='Protein', y=['Total Count', 'Unique Count'],
             title='Distribution of Binding Frequencies by Protein (Counts)',
             labels={'value': 'Count', 'variable': 'Count Type', 'Protein': 'Protein'},
             height=600)

fig.update_layout(
    xaxis_title="Protein",
    yaxis_title="Count",
    xaxis_tickangle=-90,
    bargap=0.2
)

st.plotly_chart(fig, use_container_width=True)

st.write("Sorted Protein Binding Frequencies:")
st.dataframe(sorted_data)