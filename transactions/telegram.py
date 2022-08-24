import requests

msg = "hello"
tele_auth_token = "5360510229:AAF4vATBxrOrLnynql6swCP-eBcVU4J12Mg" # Authentication token provided by Telegram bot
tel_group_id = "stockmanagementsystem"     # Telegram group name

def send_msg_on_telegram(msg):
    telegram_api_url = f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id=@{tel_group_id}&text={msg}"
    tel_resp = requests.get(telegram_api_url)
    if tel_resp.status_code == 200:
    	print ("Notification has been sent on Telegram") 
    else:
        print ("Could not send Message")
