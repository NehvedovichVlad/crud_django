from django.shortcuts import render, get_object_or_404, redirect

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
    template_name = 'accounts/person.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Person, id=id_)


def edit_person(request, id):

    person = Person.objects.get(id=id)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/edit_person.html', context)
