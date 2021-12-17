from twilio.rest import Client

TWILIO_SID = "AC1f213138843cb4f37b76972bc091a0ac"
TWILIO_AUTH_TOKEN = "131576ae3cf4c1c2bb924daf3b741ac4"
TWILIO_VIRTUAL_NUMBER = '+13156591922'
TWILIO_VERIFIED_NUMBER = '+84849396669'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
