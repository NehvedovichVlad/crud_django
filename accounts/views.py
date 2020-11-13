from django.shortcuts import render

# Create your views here.
from accounts.models import Person


def person(request):
    qs = Person.objects.all()
    context = {'persons': qs}
    return render(request, 'accounts/person.html', context)