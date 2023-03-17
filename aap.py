from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender ='malla.jayen@gmail.com'
email_password= password

email_receiver ='tinex67835@oniecan.com'


subject ="Hello I'm well and good"
body = """
When life gives you lemonade, make lemons.
Life will be all like, "Whaaaaaaaaat?"
"""
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)as smpt:
    smpt.login(email_sender,email_password)
    smpt.sendmail(email_sender,email_receiver,em.as_string())





