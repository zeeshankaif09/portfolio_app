import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("zeeshan kaif")
    content = """ hi im zeeshan kaif
    """
    st.info(content)

content2 = """
Below you can find some of the app i have built in python feel free contact me
"""
st.write(content2)