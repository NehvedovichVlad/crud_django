from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

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


class DeletePerson(DeleteView):
    template_name = 'accounts/add_person.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Person, id=id_)
