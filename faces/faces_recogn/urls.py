from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('', main_page),
              path('new', new_user),
               path('check', check),]