from django.urls import path

from .views import create_card, home_page


app_name = 'flash'
urlpatterns = [
    path('', home_page, name='home'),
    path('create', create_card, name='create'),
]