from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC7095a7f37c92f9f251b61fcc847ab524'
auth_token = '72a7a22a198f792a50507949d51c94c2'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+19284400322',
                              to='+918168176301'
                          )

print(message.sid)