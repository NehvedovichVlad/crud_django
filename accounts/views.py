from django.shortcuts import render

# Create your views here.
from accounts.models import Person


def person(request):
    qs = Person.objects.all()
    context = {'person': qs}
    return render(request, 'accounts/person.html', context)