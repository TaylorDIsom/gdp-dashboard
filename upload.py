import streamlit as st
import pandas as pd
import zipfile
from tempfile import NamedTemporaryFile

# server.maxUploadSize
# https://docs.streamlit.io/develop/api-reference/configuration/config.toml

"Upload Data"

uploaded_file = st.file_uploader("Choose a file")

"file path is:"
if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)
    with NamedTemporaryFile(dir='.', suffix='.csv') as f:
        f.write(uploaded_file.getbuffer())
        "file dir is: " + f.name
    "file path is : " + uploaded_file.name

    # with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    #     zip_ref.extractall(directory_to_extract_to)

    # Can be used wherever a "file-like" object is accepted:

# Keep this block
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)
    
    
    
    # st.line_chart(
    #     filtered_gdp_df,
    #     x='GDP',
    #     y='Year'
    # )


