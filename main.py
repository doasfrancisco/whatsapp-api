import os

from dotenv import load_dotenv
import requests

load_dotenv(override=True)

WHATSAPP_BUSINESS_ID = os.getenv("WHATSAPP_BUSINESS_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

def subscribed_apps():
    url = f"https://graph.facebook.com/v21.0/{WHATSAPP_BUSINESS_ID}/subscribed_apps"
    pass

def info_phone_number():
    url = f"https://graph.facebook.com/{PHONE_NUMBER_ID}"
    headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    response = requests.get(url, headers=headers)
    print(response.json())

def register_phone_number():
    url = f"https://graph.facebook.com/{PHONE_NUMBER_ID}/register"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    json = {
        "messaging_product": "whatsapp",
        "pin": "123456"
    }
    response = requests.post(url, headers=headers, json=json)
    print(response.json())

def create_product_update_template():
    url = f"https://graph.facebook.com/{WHATSAPP_BUSINESS_ID}/message_templates"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    json = {
    "name": "actualizacion_producto_v2",
    "language": "es",
    "category": "MARKETING",
    "parameter_format": "POSITIONAL",
    "components": [
        {
        "type": "BODY",
        "text": "¡Hola {{1}}! 😊 Espero que tenga una linda {{2}} 🫶\n\n{{3}}\n\n¡Yo seguiré aquí, atendiendo a los pacientes! 💪",
        "example": {
            "body_text": [
            [
                "Dr. Alexander","mañana","Para agendar, ahora solo necesito el motivo de la consulta, ya no hace falta la duración. Si me equivoco en un horario o en algo, avíseme porfa."
            ]
            ]
        }
        }
    ]
    }
    response = requests.post(url, headers=headers, json=json)
    print(response.json())

