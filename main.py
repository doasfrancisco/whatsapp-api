from whatsapp import dentists

import requests

def subscribed_apps(business_id: str):
    url = f"https://graph.facebook.com/v21.0/{business_id}/subscribed_apps"
    pass

def info_phone_number(phone_number_id: str, access_token: str):
    url = f"https://graph.facebook.com/{phone_number_id}"
    headers = {
    "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(url, headers=headers)
    print(response.json())

def register_phone_number(phone_number_id: str, access_token: str):
    url = f"https://graph.facebook.com/{phone_number_id}/register"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    json = {
        "messaging_product": "whatsapp",
        "pin": "123456"
    }
    response = requests.post(url, headers=headers, json=json)
    print(response.json())


if __name__ == "__main__":
    dental_office = "centro_odontologico_benavides"

    access_token = dentists[dental_office]["access_token"]
    phone_number_id = dentists[dental_office]["phone_number_id"]
    whatsapp_business_id = dentists[dental_office]["whatsapp_business_id"]

    register_phone_number(phone_number_id, access_token)

    # create_product_update_template(whatsapp_business_id, access_token)

    # templates.create_task_reminder_template(whatsapp_business_id, access_token)