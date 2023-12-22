import httpx
from rest_framework import status
from rest_framework.response import Response
from weather import settings
from rest_framework.views import APIView


class WeatherView(APIView):
    def get(self, request):
        """
        Getting the current weather in response to the name of the city.
        """
        latitude = '55.75'
        longitude = '37.62'
        response_language = settings.RESPONSE_LANGUAGE
        url = f'{settings.URL_YANDEX_WEATHER_INFORM}?lat={latitude}&lon={longitude}&lang={response_language}'
        headers = {
            'X-Yandex-API-Key': settings.API_KEY_YANDEX_WEATHER_INFORM,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        print(url)
        print(headers)
        client = httpx.Client()
        try:
            response = client.get(url, headers=headers)
            print(response)
        finally:
            client.close()
        print(f"response.wind_speed: {response.json()['wind_speed']}")
        return Response(response.wind_speed, status=status.HTTP_200_OK)
