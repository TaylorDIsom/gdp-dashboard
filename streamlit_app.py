import streamlit as st

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Taylors Stream App',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

pg = st.navigation({
    "Test": [st.Page("test.py")],
    "Data": [st.Page("download.py"), st.Page("upload.py")],
    "Misc": [st.Page("gdp.py")]
    })
pg.run()
