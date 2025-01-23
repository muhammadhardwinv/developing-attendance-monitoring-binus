import os
import requests

bot_token = "7543908439:AAFn3aK-CQLjhMVsIXgrj599i5nS4-OA35M"


def get_chat_id(bot_token, username):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
        response = requests.get(url)
        response.raise_for_status()
        updates = response.json()

        for result in updates.get("result", []):
            message = result.get("message", {})
            from_user = message.get("from", {})
            if from_user.get("username") == username:
                return from_user.get("id")

        print(f"username '{username}' not found in the recent updates.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching chat ID: {e}")
        return None


def send_message(bot_token, chat_id, text):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error code: 400, can't send message. {e}")
        return None


def validate_bot_token(bot_token):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getMe"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("ok", False)
    except requests.exceptions.RequestException as e:
        print(f"Error validating bot token: {e}")
        return False
