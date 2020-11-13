from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import PersonForm
from accounts.models import Person


def person(request):
    qs = Person.objects.all()
    context = {'persons': qs}
    return render(request, 'accounts/person.html', context)


class CreatePerson(CreateView):
    form_class = PersonForm
    template_name = 'accounts/add_person.html'
    success_url = reverse_lazy('home')
