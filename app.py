# app.py

from flask import Flask
import os
from twilio.rest import Client

app = Flask(__name__)

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')

def lambda_handler(event, context):
    print("Received event: " + str(event))
    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message>Hello world Lambada Lambda</Message></Response>'

@app.route("/")
def hello():
    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message>Hello world Lambada Lambda</Message></Response>'

@app.route("/sms/<phone>/<msg>")
def send_sms(phone, msg):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
            .create(
                body= msg,
                # "Join Earth's mightiest heroes. Like Kevin Bacon.",
                # messaging_service_sid='MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                from_='+12082739639',
                to=phone
            )

    print(message.sid)
    return f"Message {phone} Hello {msg}!"