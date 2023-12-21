from django.urls import path
from api_weather_now import views

urlpatterns = [
    path('', views.WeatherView.as_view())
]
