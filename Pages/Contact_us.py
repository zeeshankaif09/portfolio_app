import streamlit as st

st.header("Contact me")

with st.form(key="My_Forms"):
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your Message")
    button = st.form_submit_button("Sumbit")
    print(button)
    if button:
        print("Thank u for contacting us")
