from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NoteForm
from .models import Note

# Create your views here.

def notes(request):
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")
    notes = Note.objects.all()[:15]
    context = {'notes': notes}
    return render(request, 'notes/notes.html', context)

def new(request):
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Sucessfully added note")
        return redirect("notes")

    context = {'form': form}
    return render(request, 'notes/new.html', context=context)

