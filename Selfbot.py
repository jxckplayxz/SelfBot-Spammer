# BY ⌗ 🦇 C47CH-404🦇 || .gg/KK4besj8WC
import requests
import threading

# Tu Token
TOKEN = "MTQ4NjM2MzUyNzI5MDY4MzQ2Mw.GNzaaS.qIjYgF1sOq7N19SjsLOsYA0IygjeN60ABcS124"

# IDs de los canales a los que quieres hacer spam
CHANNEL_IDS = [
    "1426761744935813163",  # Canal 1
    "1426761744935813163",  # Canal 2
    "1426761744935813163"   # Canal 3
]

# Mensaje a enviar
MESSAGE = ""

# Cantidad de mensajes
AMOUNT = 20000

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

BASE_URL = "https://discord.com/api/v9/channels"

def send_messages(channel_id):
    print(f"Iniciando spam en el canal {channel_id}...")

    for i in range(AMOUNT):
        payload = {"content": MESSAGE}
        url = f"{BASE_URL}/{channel_id}/messages"
        response = requests.post(url, headers=HEADERS, json=payload)

        if response.status_code == 200:
            print(f"Canal {channel_id}: Enviado mensaje {i+1}/{AMOUNT}")
        else:
            print(f"Canal {channel_id}: Error al enviar mensaje: {response.status_code} - {response.text}")

threads = []
for channel_id in CHANNEL_IDS:
    thread = threading.Thread(target=send_messages, args=(channel_id,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("OWNED BY ⌗ 🦇 C47CH-404🦇 || .gg/KK4besj8WC")
