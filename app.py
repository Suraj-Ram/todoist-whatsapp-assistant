from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from pydub import AudioSegment
import speech_recognition as sr
import todoist_interface as ti

app = Flask(__name__)

@app.route('/incoming_test', methods=["POST"])
def incoming_test():
    body = request.values.get('Body', None)
    resp_msg = MessagingResponse()

    if body.lower() == "what are my tasks for today?":
        print("Tasks for today requested")
        resp_msg.message("Task1, 2, 3, 4, 5, ...")
    else:
        resp_msg.message("Send a suitable message")

    return str(resp_msg)

