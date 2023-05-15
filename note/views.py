from django.shortcuts import render, redirect
from .models import Note

# Create your views here.

def index(request):
    note = Note.objects.all()
    
    context = {'note':note}
    
    return render(request, "note/index.html", context)

def note(request):
    if request.method == "POST":
        note_heading = request.POST.get('note_heading')
        note_des = request.POST.get('note_des')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        
        note = Note(
            note_heading=note_heading,
            note=note_des,
            lat=lat,
            lng=lng
        )
        note.save()
        return redirect('/map')
    
    context = {}
    
    return render(request, "note/index.html",context)