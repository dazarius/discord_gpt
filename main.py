import requests
import json
import re
import time
import ai
import datetime
from currency_converter import CurrencyConverter
import asyncio


c = CurrencyConverter()

##payload from sent msg on disco
headers = {
    "Authorization": "<token>",
    "Content-Type": "application/json",
}
lastId = []
lastMsgId = []  # Предполагается, что у вас уже определена переменная lastMsgId
openai = ai.AI("<api_openai>")






def member_id():
    url = "https://discord.com/api/v9/guilds/1080817368646819941/members-search"
    response = requests.post(url, headers=headers)
    data = response.json()
    return data


def chat_gpt():
    url_wiretap = "https://discord.com/api/v9/channels/1238122520364712019/messages?limit=1"
    response = requests.get(url_wiretap, headers=headers)
    data = response.json()

    message = data[0] 
    message_id = message["id"]
    author_id = message["author"]["id"]
    message_content = message["content"]
    mentions = message["mentions"]
    referenced_msg = message.get("referenced_message")
    
    time.sleep(2)
    # Проверяем, не относится ли сообщение к нужному автору
    if  message_content.startswith("?"):
            # Генерируем ответ с помощью OpenAI
            with open("alowed_channel_id.json", "r") as f:
                data = json.load(f)
                if author_id in data["members"]:
                            
                    try:        
                        ask_chat = openai.generate(message_content)

                        payload_msg = {
                            "content": ask_chat + "\n\n",
                            
                        }
                                    # Отправляем ответ обратно на Discord
                        edit = requests.patch(f"https://discord.com/api/v9/channels/1238122520364712019/messages/{message['id']}", headers=headers, json=payload_msg)
                    except Exception as e:
                        print(e)
            
    if message_content.startswith("="):

        with open("alowed_channel_id.json", "r") as f:
            data = json.load(f)
            if author_id in data["members"] and message_id not in lastMsgId:
                lastMsgId.append(message_id)
                convert = message_content.split(" ")
                amount = convert[1]
                from_currency = convert[2]
                to_currency = convert[3]
                try:
                    payload = {
                        "content": f"{c.convert(amount, from_currency.upper(), to_currency.upper())}\n\n",
                    }
                    
                    edit = requests.patch(f"https://discord.com/api/v9/channels/1238122520364712019/messages/{message['id']}", headers=headers, json=payload)
                except:
                    pass
    if message_content.startswith("$"):
        with open("alowed_channel_id.json", "r") as f:
            data = json.load(f)
            if author_id in data["members"] and message_id not in lastMsgId:
                lastMsgId.append(message_id)
                
# def announcment_check():
#     with open("announcment_msg_id.txt", "r") as f:
#         file = f.read()
#     with open("announcment_list.json", "r") as f:
#         announcment_list = json.load(f)
#         for key, value in announcment_list.items():
#             url = f"https://discord.com/api/v9/channels/{value}/messages?limit=1"
            
#             response = requests.get(url, headers=headers)
#             data = response.json()
            
#             msg = data[0]["content"]
#             msg_id = data[0]["id"]
#             if msg_id not in file:
#                 with open("announcment_msg_id.txt", "a") as f:  # Open file in append mode
#                     f.write(msg_id + "\n")  # Add a newline character
                
#                 ru = openai.generate(f"переведи пожалуйста это сообщение на русский язык, но не переводи слова с @: {msg}")            
#                 with open(f"announcment/{key}_{datetime.datetime.now()}.txt", "w") as f:
#                     f.write(ru)
                
#                 print(f"Announcment {key} is done!")



#                 time.sleep(5)
#             else:
#                 pass            
            
        


def main():
    while True:
        chat_gpt()
if __name__ == "__main__":

    main()