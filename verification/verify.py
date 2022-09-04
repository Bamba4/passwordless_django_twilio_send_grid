from twilio.rest import Client
from django.conf import settings

class SendOTP:
    def send_code(receiver):
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = Client(account_sid, auth_token)
        print(receiver, account_sid, auth_token, client)

        verification = client.verify \
                     .services(settings.SERVICE_ID) \
                     .verifications \
                      .create(channel_configuration={
                           'template_id': settings.TEMPLATE_ID,
                           'from': settings.DEFAULT_FROM_EMAIL,
                           'from_name': 'Bamba Diagne'
                       }, to=receiver, channel='email')
        print(verification)
        return verification.status