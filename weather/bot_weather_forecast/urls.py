from django.urls import path
from bot_weather_forecast.views import webhook

urlpatterns = [
    path('', webhook, name='webhook')
]
