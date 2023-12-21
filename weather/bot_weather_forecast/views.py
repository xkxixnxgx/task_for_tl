from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from weather import settings
import httpx


@api_view(['GET'])
def weather_forecast(request):
    """
    Getting the current weather in response to the name of the city.
    """
    latitude = 55.75
    longitude = 37.62
    response_language = settings.get('RESPONSE_LANGUAGE', 'ru_RU')
    url = settings.URL_YANDEX_WEATHER \
        .replace('<latitude>', latitude) \
        .replace('<longitude>', longitude) \
        .replace('<response_language>', response_language)
    headers = {
        'X-Yandex-API-Key': settings.API_KEY_YANDEX_WEATHER
    }
    client = httpx.Client()
    try:
        response = client.get(url, headers=headers)
    finally:
        client.close()
    print(f"response.wind_speed: {response.json()['wind_speed']}")
    return Response(response.wind_speed, status=status.HTTP_200_OK)
