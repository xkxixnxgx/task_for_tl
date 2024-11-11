import httpx
from weather import settings

APP_HOST_FOREIGN = 'https://' + settings.APP_HOST_FOREIGN

# telegram url
TELEGRAM_API_URL = settings.TELEGRAM_API_URL
TOKEN = settings.TELEGRAM_BOT_TOKEN
URL = TELEGRAM_API_URL + TOKEN + "/"

# example set and delete Webhook
# https://api.telegram.org/bot<TOKEN>/deleteWebhook
# https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://8361-185-94-174-210.ngrok.io/webhook/
URL_REMOVE_WEBHOOK = URL + "deleteWebhook"
URL_SET_WEBHOOK = URL + "setWebhook?url=" + APP_HOST_FOREIGN + "/webhook/"
URL_WEBHOOK_INFO = URL + 'getWebhookInfo'


def reset_telegram_webhook(
    URL_REMOVE_WEBHOOK,
    URL_SET_WEBHOOK,
    URL_WEBHOOK_INFO,
) -> None:
    httpx.get(URL_REMOVE_WEBHOOK)
    httpx.get(URL_SET_WEBHOOK)
    res = httpx.get(URL_WEBHOOK_INFO)
    webhook_info = None
    if res.text:
        webhook_info = res.text
    return webhook_info


def print_status_init(
    URL_REMOVE_WEBHOOK,
    URL_SET_WEBHOOK,
    WEBHOOK_INFO,
) -> None:
    print(f"TELEGRAM WEBHOOK WAS REMOVED: {URL_REMOVE_WEBHOOK}")
    print(f"TELEGRAM WEBHOOK WAS SET: {URL_SET_WEBHOOK}")
    print(f"TELEGRAM WEBHOOK INFO: {WEBHOOK_INFO}")
    return


WEBHOOK_INFO = reset_telegram_webhook(
    URL_REMOVE_WEBHOOK,
    URL_SET_WEBHOOK,
    URL_WEBHOOK_INFO,
)
print_status_init(
    URL_REMOVE_WEBHOOK,
    URL_SET_WEBHOOK,
    WEBHOOK_INFO,
)
