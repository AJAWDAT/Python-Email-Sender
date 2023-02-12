#E-Mail Sender

from email.message import EmailMessage
import ssl
import smtplib

sender=#edited out for security reasons
password=#edited out for security reasons

receiver=#edited out for security reasons

subject='Important News'
body='''
Our resident represenative has been fired because he didn't do anything, \
we had no choice but to replace him with a baby who we are sure will be \
atleast as competent.
'''

em=EmailMessage()
em['From']=sender
em['To']=receiver
em['Subject']=subject
em.set_content(body)

context= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,em.as_string())

