from threading import Thread
from twilio.rest import Client


class SendOtpThread(Thread):

    def __init__(self, otp, phone):
        Thread.__init__(self)
        self.otp = otp
        self.phone = phone

    def run(self):
        try:
            account_sid = 'AC8b5ead76bcce5709a6edddf570cbe9d4'
            auth_token = 'a32f6ddb034bcb9777aecf62ecfc026b'
            client = Client(account_sid, auth_token)

            client.messages.create(
                body=f'{self.otp} is your one time password(OTP) for phone verification by Grofusion.com',
                from_='+13366523298',
                to= '+91' + self.phone)

        except:
            pass