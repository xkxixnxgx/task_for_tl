import httpx
from weather import settings

APP_HOST_FOREIGN = 'https://' + settings.APP_HOST_FOREIGN

# telegram urls
TELEGRAM_API_URL = settings.TELEGRAM_API_URL
TOKEN = settings.TELEGRAM_BOT_TOKEN
URL = TELEGRAM_API_URL + TOKEN + "/"


def reset_telegram_webhook() -> None:
    # example set and delete Webhook
    # https://api.telegram.org/bot<TOKEN>/deleteWebhook
    # https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://8361-185-94-174-210.ngrok.io/webhook/
    URL_REMOVE_WEBHOOK = URL + "deleteWebhook"
    URL_SET_WEBHOOK = (
        URL
        + "setWebhook?url="
        + APP_HOST_FOREIGN
        + "/webhook/"
    )
    URL_INFO_WEBHOOK = URL + 'getWebhookInfo'

    httpx.get(URL_REMOVE_WEBHOOK)
    print(f"TELEGRAM WEBHOOK WAS REMOVED: {URL_REMOVE_WEBHOOK}")
    httpx.get(URL_SET_WEBHOOK)
    print(f"TELEGRAM WEBHOOK WAS SET {URL_SET_WEBHOOK}")
    info = httpx.get(URL_INFO_WEBHOOK)
    print(f"TELEGRAM WEBHOOK INFO {info.text}")
    return


reset_telegram_webhook()