import streamlit as st
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user_name = "zeeshankaif09@gmail.com"
    password = "Password"
    receiver = "zeeshankaif09@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)



send_email()