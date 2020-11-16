from django.urls import path

from .views import *


urlpatterns = [
    path('', person, name='home'),
    path('add_person/', CreatePerson.as_view(), name='add_person'),
    path('<int:id>/delete/', DeletePerson.as_view(), name='delete_person'),
    path('edit_person/<int:id>', edit_person, name='edit_person')
]
