import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

"Download Data"

@st.cache_data
def get_data():
    # df = pd.DataFrame(
    #     np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
    # )
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)
    # df = gdp_df
    return raw_gdp_df

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")


df = get_data()

st.write(df)

csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)
