import os
from twilio.rest import Client
from django.conf import settings

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

class CheckOTP:
    
    def check_otp(phone_number, secret):
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = Client(account_sid, auth_token)
        verification_check = client.verify \
                           .services(settings.SERVICE_ID)\
                           .verification_checks \
                           .create(to=phone_number, code=secret)

        return verification_check.status
