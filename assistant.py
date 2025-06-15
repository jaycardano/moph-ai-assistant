import requests
import os
from dotenv import load_dotenv

load_dotenv()

HASS_URL = os.getenv("HASS_URL")
TOKEN = os.getenv("TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def turn_on_tv():
    entity_id = "media_player.family_room_tv"
    url = f"{HASS_URL}/services/media_player/turn_on"
    data = {"entity_id": entity_id}
    resp = requests.post(url, headers=HEADERS, json=data)
    print(f"Turn on TV: {resp.status_code} - {resp.text}")

def main():
    print("Stim AI Assistant Ready")
    while True:
        cmd = input("Enter a command (tv_on/exit): ").strip()
        if cmd == "tv_on":
            turn_on_tv()
        elif cmd == "exit":
            print("Exiting.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
