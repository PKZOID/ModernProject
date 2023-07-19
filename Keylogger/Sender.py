import requests
import json

webhook_url = 'Your Web hook Discrod Url'

message = {
    'content':"Hello World",
    'username':"Bot"
}

payload = json.dumps(message)

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(webhook_url, data=payload, headers=headers)

if response.status_code == 204:
    print('Message sent successfully!')
else:
    print(f'Failed to send message. Error: {response.text}')
