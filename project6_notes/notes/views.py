from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes


# Create your views here.

def notes_list_views(request):
    # return HttpResponse("test")
    note = Notes.objects.all()
    print(note)
    context = {
        'note': note
    }
    return render(request, template_name='notes/note_list.html', context=context)


