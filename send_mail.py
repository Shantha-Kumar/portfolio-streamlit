import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "shand.luffy@gmail.com"
password = "gkdzzyxnuskmkueq"
receiver = "shand.luffy@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Hi :)
How ru ?
Bye!!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
