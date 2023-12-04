import json
import logging
import requests

import azure.functions as func
from azure.cosmos import CosmosClient


endpoint = "https://proj-db-esp8266.documents.azure.com:443/"
key = "Kxp4PLYc5NyNrILQT8hpLgNM9GV13VZtKyMVj7B0v9aHQH1KMEjKdK7HTiHYIlsSayaqYxhBsweMACDbWjy2rQ=="
database_id = "ToDoList"
container_id = "Items"
telegram_token = "token från telegram"
chat_id = "chat?id"



def main(event: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event: %s', event.get_json())

    logging.info("Loggar data: %s", event)

    device_id = event.get_json().get("data", {}).get("deviceId")

    message = event.get_json()["body"] 

    telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"

    try:
        response = requests.get(telegram_url)
        response.raise_for_status()
        logging.info("Telegram response: %s", response.text)
    except requests.exceptions.RequestException as e:
        logging.error("Error sending message to Telegram: %s", e)

