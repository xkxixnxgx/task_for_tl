import json
from weather import settings
import httpx
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Updater, filters

TELEGRAM_API_URL = settings.TELEGRAM_API_URL
TELEGRAM_BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
URL = f'{TELEGRAM_API_URL}{TELEGRAM_BOT_TOKEN}'


# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Привет!')

# def button_pressed(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Привет по нажатию кнопки!')

def send_message(chat_id, text):
    url = f'{URL}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    httpx.post(url, json=data)

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        chat_id = data['message']['chat']['id']
        text = data['message']['text']
        print(f"Входящее сообщение: {text}")
        # bot_token = TELEGRAM_BOT_TOKEN
        # updater = Updater(bot_token)
        # dp = updater.dispatcher

        # dp.add_handler(CommandHandler("start", start))
        # dp.add_handler(MessageHandler(filters.BaseFilter.Regex(r'Нажать кнопку'), button_pressed))

        # # Start the Bot
        # updater.start_polling()
        if text == '/start':
            send_message(chat_id, 'Привет! Жми "Узнать погоду".')

        # elif text == 'Узнать погоду':
        #     weather_data = get_weather()
        #     send_message(chat_id, f'Погода сегодня: {weather_data}')

        return JsonResponse({'status': 'ok'})



def get_weather():
    # latitude = '55.75'
    # longitude = '37.62'
    # response_language = settings.RESPONSE_LANGUAGE
    # url = f'{settings.URL_YANDEX_WEATHER_FORECAST}?lat={latitude}&lon={longitude}&lang={response_language}'
    # headers = {
    #     'X-Yandex-API-Key': settings.API_KEY_YANDEX_WEATHER_FORECAST,
    #     'Accept': 'application/json',
    #     'Content-Type': 'application/json',
    # }
    # print(url)
    # print(headers)
    # client = httpx.Client()
    # try:
    #     response = client.get(url, headers=headers)
    #     print(response)
    # finally:
    #     client.close()
    # print(f"response.wind_speed: {response.json()['wind_speed']}")
    # return JsonResponse(response.wind_speed)
    return "Okkk"

# def get_keyboard():
#     button = KeyboardButton("Узнать погоду")
#     reply_markup = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
#     return reply_markup

