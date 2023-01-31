import requests
import constants as keys

def send_message(chat_id, text):
    token = "5423008564:AAHwNI93fqXkVpUQ6bkJuvn4lEvfBoeagnc"

    url = "https://api.telegram.org/bot" + token + "/sendmessage" + "?chat_id=" + str(chat_id) + "&text=" + text
    results = requests.get(url)
    print(results.json())

send_message(939184869, "Hello")