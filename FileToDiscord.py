import requests

# Replace WEBHOOK_URL with your Discord webhook URL
WEBHOOK_URL = "Your_Discord_Url"

def send_message_to_discord(message):
    data = {"content": message}
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code != 204:
            print(f"Error sending message to Discord: {response.status_code} {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Discord: {e}")

def send_file_to_discord(file_path):
    try:
        with open(file_path, "rb") as file:
            data = {"file": file}
            response = requests.post(WEBHOOK_URL, files=data)
            if response.status_code != 204:
                print(f"Error sending file to Discord: {response.status_code} {response.reason}")
    except IOError as e:
        print(f"Error reading file: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending file to Discord: {e}")

def send_message_and_file_to_discord(message):
    file_path = input("Enter the path to the file: ")
    send_message_to_discord(message)
    send_file_to_discord(file_path)

send_message_and_file_to_discord("This is a File")
