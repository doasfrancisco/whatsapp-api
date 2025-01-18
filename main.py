import os

from dotenv import load_dotenv
import requests

load_dotenv(override=True)

access_token = os.getenv("ACCESS_TOKEN")
phone_number_id = os.getenv("PHONE_NUMBER_ID")

print(access_token, phone_number_id)

# # url = f"https://graph.facebook.com/{phone_number_id}"
# url = f"https://graph.facebook.com/{phone_number_id}/register"
# headers = {
#     "Authorization": f"Bearer {access_token}",
# }
# json = {
#     "messaging_product": "whatsapp",
#     "pin": "123456"
# }
# response = requests.post(url, headers=headers, json=json)
# # response = requests.get(url, headers=headers)
# print(response.json())