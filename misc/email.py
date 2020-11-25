# --- built in ---
import os
import sys
import json
import time
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SECRET = None

def formatter(template, **kwargs):
    return template.format(**kwargs)

def setTemplate(template, formatter=formatter):
    '''
    Email template

    template: template file (*.html)
    formatter: a function to format template (default will use str.format)
    '''

    global SECRET

    if template is not None:
        with open(template, 'r') as f:
            SECRET['template'] = f.read()
            
    SECRET['formatter'] = formatter

def loadConfig(secret, template=None, formatter=formatter):
    '''
    Load gmail configurations from file

    sender: 'oooooo@gmail.com'
    password: 'xxxxxxxxxxx'
    smtp_ip: 'smtp.gmail.com' (Optional)
    smtp_port: 465 (Optional)
    targets: ['xxx001@gmail.com', 'xxx002@gmail.com'] (Optional)
    '''

    global SECRET
    with open(secret, 'r') as f:
        SECRET = json.load(f)

    assert SECRET.get('sender') and SECRET.get('password')

    SECRET['smtp_ip'] = SECRET.get('smtp_ip', 'smtp.gmail.com')
    SECRET['smtp_port'] = SECRET.get('smtp_port', 465)

    setTemplate(template, formatter)

    if SECRET.get('targets'):
        if isinstance(SECRET['targets'], str):
            SECRET['targets'] = [SECRET['targets']]
        assert isinstance(SECRET['targets'], list), 'targets must be a list of str'
    

def send(contents=None, 
         targets=None,
         subject=None, **kwargs):
    '''
    Send message
    '''

    global SECRET
    assert SECRET is not None, 'Call loadConfig first'

    if subject is None:
        subject = '[Blank]'

    # user information
    sender = SECRET['sender']
    password = SECRET['password']
    
    # email targets
    if targets is None:
        assert SECRET.get('targets'), 'Targets not specified'
    
        targets = SECRET['targets']

    targets = ', '.join(targets)

    # email template and formatter
    template = SECRET.get('template')
    formatter = SECRET.get('formatter')

    # create email
    mail = MIMEMultipart()
    mail['Subject'] = subject
    mail['From'] = sender
    mail['To'] = targets

    # format message
    if template:
        message = formatter(template, contents=contents,
                                      targets=targets,
                                      subject=subject,
                                      **kwargs)
    else:
        message = '{}'.format(contents)

    # attach message to email
    mail.attach(MIMEText(message, 'html'))

    # send email
    server = smtplib.SMTP_SSL(SECRET['smtp_ip'], SECRET['smtp_port'])
    server.login(SECRET['sender'], SECRET['password'])
    server.sendmail(sender, targets, mail.as_string())
    server.quit()