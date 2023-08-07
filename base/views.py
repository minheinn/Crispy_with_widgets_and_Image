from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    persons = Person.objects.all()
    context = {'persons':persons}
    return render(request, 'pages/index.html', context)

def AddPerson(request):
    forms = PersonForm()
    if request.method == "POST":
        forms = PersonForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Add Person is successfully!")
            return redirect('show_person')
    context = {'forms':forms}
    return render(request, 'pages/AddPerson.html', context)

def UpdatePerson(request, pk):
    person = Person.objects.get(id=pk)
    forms = PersonForm(instance=person)
    if request.method == "POST":
        forms = PersonForm(request.POST, request.FILES, instance=person)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Update Person is successfully!")
            return redirect('show_person')
    context = {'person':person, 'forms':forms}
    return render(request, 'pages/UpdatePerson.html', context)

def DeletePerson(request, pk):
    persons = Person.objects.all()
    person = Person.objects.get(id=pk)
    person.delete()
    messages.success(request, "Delete Person is successfully!")
    context = {'persons':persons, 'person':person}
    return render(request, 'pages/index.html', context)