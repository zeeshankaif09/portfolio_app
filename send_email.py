import smtplib, ssl

host="smtp.gmail.com"
port = 465

user_name ="zeeshankaif09@gmail.com"
password = "take it password from gmail"

receiver = "zeeshankaif09@gmail.com"
context = ssl.create_default_context()

message = """ \
subject: hi how are you 
bye!
"""
with smtplib.SMTP_SSL(host, port, context=context)as server:
    server.login(user_name, password)
    server.sendmail(user_name, receiver, message)