import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Shantha Kumar")
    content = """
    Hi :) My name is Shantha Kumar . I'm trying to get better. I completed my bachelor's in 2022 in computer science. 
    I'm just starting.
        """
    st.info(content)

content2 = """Below listed are few of my projects that I have built."""
st.subheader(content2)
