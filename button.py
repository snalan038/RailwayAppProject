from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello, this is a test message!',
    from_='your_twilio_phone_number',
    to='recipient_phone_number'
)

print(message.sid)
