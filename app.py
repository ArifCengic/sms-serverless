# app.py

from flask import Flask
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'

app = Flask(__name__)

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sms/<phone>/<message>")
def send_sms(phone, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
            .create(
                body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                # messaging_service_sid='MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                from_='+12082739639',
                to='+12027511880'
            )

    print(message.sid)
    return f"Message ${phone} Hello ${message}!"