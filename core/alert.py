# core/alert.py
import requests

def send_telegram_alert(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"[!] Gagal mengirim alert Telegram: {response.text}")
    except Exception as e:
        print(f"[!] Error saat mengirim Telegram alert: {e}")
