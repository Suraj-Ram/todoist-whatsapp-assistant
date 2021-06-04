# Todoist Whatsapp Assistant

A Python Flask service that interfaces with the Twilio Whatsapp API to get and add **Todoist** tasks by speech* and through messages (where both are sent through Whatsapp).

## Setup

**1.** Add your Todoist API token as the `TODOIST_API_TOKEN` environment variable. 

*You can find your token from the Todoist Web app, under Todoist Settings -> Integrations -> API token.*

**2.** Install modules
```bash
pip install -r requirements.txt
```


**3.** Run the flask app.
```bash
python -m flask run
```
**4.** Use `ngrok` or a similar tool to expose local port to the internet

**5.** Log into the Twilio Console and paste ngrok URL into the "WHEN A MESSAGE COMES IN" field

**6.** Follow the Twilio-provided instructions to connect to the Twilio Sandbox through Whatsapp

## Usage
Simply send a message to the Twilio Sandbox phone number

**Speech recognition coming soon*