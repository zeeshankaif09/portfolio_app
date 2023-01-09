import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="My_Forms"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    options = st.selectbox("What Topic you want to disscuss",('job inquiries','project propsal','other'))
    st.write('You selected:', option)
    message = f""" \n
    Subject: new message from{user_email}
    
    From:{user_email}
    {raw_message}
    """
    button = st.form_submit_button("Sumbit")
    print(button)
    if button:
        send_email(message)
        st.info("your email sent successfully")

