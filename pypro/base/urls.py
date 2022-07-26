from django.urls import path

from pypro.base.views import home, testez


app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('testez',testez,name='testez')
]