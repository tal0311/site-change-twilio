from twilio.rest import Client

def send_whatsapp_message(msg):
    
    account_sid = '[Account SID]'
    auth_token = '[Auth Token]'
    client = Client(account_sid, auth_token)

    if msg:
        body = msg
    else:
        body = "Site you are watching has not changed"

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=body,
        to='whatsapp:+972543113309'
    )
    print("Message id:", message.sid)
