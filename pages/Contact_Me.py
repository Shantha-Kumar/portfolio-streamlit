import streamlit as st

st.header("Contact Me")

with st.form(key = 'contact_form'):
    st.text_input(label='Enter Your Mail Address')
    st.text_area(label='Enter Your Message')
    button = st.form_submit_button(label='Submit')
    if button:
        print("pass")