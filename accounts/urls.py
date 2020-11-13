from django.urls import path

from .views import *


urlpatterns = [
    path('', person, name='home'),
    path('add_person/', CreatePerson.as_view(), name='add_person'),
]
