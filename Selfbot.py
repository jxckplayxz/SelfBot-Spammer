import requests
import threading
import time

# Fetch token from the website
print("Fetching token from the website...")
response = requests.get("https://never212.neocities.org/")
if response.status_code == 200:
    TOKEN = response.text.strip()
    print("Token successfully fetched!")
else:
    print(f"Failed to fetch token: {response.status_code}")
    exit()

# Discord channel ID
CHANNEL_IDS = [
    "1426761744935813163"
]

# Improved message
MESSAGE = "@everyone I found a website where you can stream TV shows, movies, and live football/soccer games 🔥\nhttps://xello-streams.vercel.app/"

# Number of messages to send
AMOUNT = 20

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

BASE_URL = "https://discord.com/api/v9/channels"

def send_messages(channel_id):
    print(f"Starting spam in channel {channel_id}...")

    for i in range(AMOUNT):
        payload = {"content": MESSAGE}
        url = f"{BASE_URL}/{channel_id}/messages"
        response = requests.post(url, headers=HEADERS, json=payload)

        if response.status_code == 200:
            print(f"Channel {channel_id}: Message {i+1}/{AMOUNT} sent successfully")
        else:
            print(f"Channel {channel_id}: Failed to send message: {response.status_code} - {response.text}")
        
        # Small delay to reduce rate limit risk
        time.sleep(0.8)

threads = []
for channel_id in CHANNEL_IDS:
    thread = threading.Thread(target=send_messages, args=(channel_id,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("OWNED BY ⌗ 🦇 C47CH-404🦇 || .gg/KK4besj8WC")
