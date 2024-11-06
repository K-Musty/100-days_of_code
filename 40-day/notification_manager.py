from twilio.rest import Client
SID = ""
AUTH_TOKEN = ""



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="",
            to="",
        )
        # Prints if successfully sent.
        print(message.sid)
