import serial
import requests
from twilio.rest import Client
import json
from urllib.request import urlopen

account_sid = "AC44899e687936f77a4db552a857c7f10e"
auth_token = "5c2396ffb5e6527c6eac0471282b997f"
twilio_number = "+14179323772"
recipient_number = "+918919XXXXXX"

serial_port = "COM5"  # Update with your serial port
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate, timeout=1)

api_key = "8OERWHRMPKTWQLHL"  # Replace with your ThingSpeak API key
url = f"https://api.thingspeak.com/update.json"
count = 0

client = Client(account_sid, auth_token)
message_sent = False  # Flag to track if message has been sent

while True:
    line = ser.readline().decode().strip()

    if line == "":
        line = 0
    elif line != "":
        line = int(line)

    print(line)

    count = count + 1
    if count == 70:
        payload = {"api_key": api_key, "field1": line}
        response = requests.get(url, params=payload)
        count = 0

    if not message_sent and line > 350:
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        data = json.load(response)
        x = f'driver is drunk at city: {data["city"]}, region: {data["region"]}, country: {data["country"]}, Lat & Long: {data["loc"]}'
        message = client.messages.create(
            body=x, from_=twilio_number, to=recipient_number
        )
        print("Message sent successfully!")
        message_sent = True

# Close the serial port
ser.close()
