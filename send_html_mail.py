import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("./index.html").read_text())

email = EmailMessage()
email['from'] = "<name of sender>"
email['to'] = '<recipient email id>'
email['subject'] = 'lets try sending mails using python!'

email.set_content(html.substitute({'name':'<actual name in html content>'}),'html')

#this is gmail smtp config
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	print('connecting to smtp server...')
	smtp.ehlo()
	print('starting tls...')
	smtp.starttls()
	print('login to server...')
	#login with from account
	#to use gmail to send mails from please enable less secure apps in gmail account settings
	smtp.login('<login email id>','<password of sender email>')
	print('sending mail...')
	smtp.send_message(email)
	print('email is submitted to SMTP server succesfully.\nHappy mailing :)')