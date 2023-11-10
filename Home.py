import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.WEBP")

with col2:
    st.title("Shantha Kumar")
    content = """
    Hi :) My name is Shantha Kumar . I'm trying to get better. 
    I'm just starting.
        """
    st.info(content)

content2 = """Below listed are few of my projects that I have built."""
st.subheader(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[sourcecode]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[sourcecode]({row['url']})")


