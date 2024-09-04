import os
import numpy as np
import pandas as pd
import streamlit as st

# Start streamlit app
st.sidebar.title('SELEX Data Explorer')
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

    code = '''$ find . -name "*.gz" | grep -v "ZeroCycle" | wc -l 
2069
$ find . -name "*.gz" | grep "ZeroCycle" | wc -l
441'''
    st.code(code, language="bash")

