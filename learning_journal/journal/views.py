from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Entry

# Create your views here.
def index(request):
    entries = Entry.objects.all()
    return render(request, 'journal/index.html', {'entries': entries})


class EntryDetailView(DetailView):
    model = Entry
