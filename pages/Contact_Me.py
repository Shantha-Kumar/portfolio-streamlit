import streamlit as st
from send_mail import send_mail
st.header("Contact Me")

with st.form(key='contact_form'):
    user_mail = st.text_input(label='Enter Your Mail Address')
    raw_message = st.text_area(label='Enter Your Message')
    message = f"""\
Subject: New Mail From {user_mail}

Mail ID: {user_mail}
{raw_message}
"""
    button = st.form_submit_button(label='Submit')
    print(message)
    if button:
        send_mail(message)
        st.info("Your Email Was Successfully Sent")
