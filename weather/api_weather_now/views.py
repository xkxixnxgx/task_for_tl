import json
import httpx
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from weather import settings
from pprint import pprint


class WeatherView(APIView):
    # @method_decorator(cache_page(60 * 30))
    def get(self, request):
        """
        Getting the current weather in response to the name of the city.
        """
        # transform city to coordinates
        # https://geocode-maps.yandex.ru/1.x/?apikey=YOUR_API_KEY&geocode=Tverskaya+6&lang=en_US&format=json
        # {
        #     GeocoderResponseMetaData:
        #         {
        #             "request": "E134.854,S25.828",
        #             "found": "1",
        #             "results": "10",
        #             "Point":
        #             {
        #                 "pos": "134.854412 -25.828084",
        #             }
        #         }
        # }
        city = 'Самара'
        response_language = settings.RESPONSE_LANGUAGE
        url = f'{settings.URL_YANDEX_GEOCODER}?apikey={settings.API_KEY_YANDEX_GEOCODER}&geocode={city}&lang={response_language}&format=json'
        print(url)
        client = httpx.Client()
        try:
            response = client.get(url)
            found_cityes = response.json()['response']['GeoObjectCollection']['featureMember']
            # def filter_region(items):
            #     filtering_result = []
            #     for item in items:
            #         if 
            # found_cityes = filter(filter_region, found_cityes)

            
            
            found_cityes = filter(
                lambda item: item['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['country_code'] == "RU",
                found_cityes.copy()
            )
            for item in found_cityes:
                pprint(item, width=4)
        finally:
            client.close()
        # print(f"response.wind_speed: {response.json()['wind_speed']}")
        return response

        # get weather
        # latitude = '55.75'
        # longitude = '37.62'
        # response_language = settings.RESPONSE_LANGUAGE
        # url = f'{settings.URL_YANDEX_WEATHER_INFORM}?lat={latitude}&lon={longitude}&lang={response_language}'
        # headers = {
        #     'X-Yandex-API-Key': settings.API_KEY_YANDEX_WEATHER_INFORM,
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
        # return Response(response.wind_speed, status=status.HTTP_200_OK)
