import smtplib
from email.message import EmailMessage
#from string import Template
#from pathlib import Path

#html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Aiden Tran'
email['to'] = 'raymondhieutran@gmail.com'
email['subject'] = 'Hello Minh Hieu, hope you have a nice day'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send_message(email)
    print('all good sir')
