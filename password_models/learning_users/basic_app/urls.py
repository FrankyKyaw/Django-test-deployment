from django.urls import path, include, re_path
from basic_app import views

# TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns = [
    path('register/',views.registration, name='registration'),
    path('user_login/',views.user_login,name="user_login"),
]