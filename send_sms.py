from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

my_msg = "Your message goes here"

# Sending SMS message - sends a SMS to 'to'
message = client.messages.create(from_ = my_twilio,
                                 to = my_cell,
                                 body=my_msg)

print(message.sid)
