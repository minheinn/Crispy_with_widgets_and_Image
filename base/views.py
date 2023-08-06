from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

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
            return redirect('show_person')
    context = {'forms':forms}
    return render(request, 'pages/AddPerson.html', context)