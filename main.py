import os

from dotenv import load_dotenv
import requests

load_dotenv(override=True)

WHATSAPP_BUSINESS_ID = os.getenv("WHATSAPP_BUSINESS_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

# print(access_token, phone_number_id)

# url = f"https://graph.facebook.com/{phone_number_id}"
# url = f"https://graph.facebook.com/{phone_number_id}/register"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
}
# json = {
#     "messaging_product": "whatsapp",
#     "pin": "123456"
# }
# response = requests.post(url, headers=headers, json=json)
# # response = requests.get(url, headers=headers)



url = f"https://graph.facebook.com/v21.0/{WHATSAPP_BUSINESS_ID}/subscribed_apps"
response = requests.get(url, headers=headers)
print(response.json())