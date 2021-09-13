import smtplib
from email.message import EmailMessage
 
# instantiate an EmailMessage class to an email object
email = EmailMessage()
# add to this object the 'from' key to say who this email is from
email['from'] = 'Interaculant'
# who this email is going to be to
email['to'] = 'bobw10294@gmail.com'
# email subject line
email['subject'] = 'You won 1,000,000 dollars!'
 
# set_content method, allows you to send contents or messages. You can send text, html, images
email.set_content('I am a Python Master!')
 
# sending the email by using smtp to login to our gmail client and then send the email from there
# custom to whatever email client you're using 
# host is going to be gmail running on port 587
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # part of the protocol of the smtp agreement
    smtp.ehlo()
    # tls is an encrption system to connect securely to the server
    smtp.starttls()
    #login with email and password
    smtp.login('interaculant@gmail.com', 'Interact12345')
    #send email
    smtp.send_message(email)