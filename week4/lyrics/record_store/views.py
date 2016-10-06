from django.shortcuts import render
from record_store.models import Song
import datetime
# Create your views here.
def index_view(request):
    context = {
        "my_name": "Joel Money Yeeeeyah!!!",
        "now": datetime.datetime.now(),
        "all_songs": Song.objects.all()
    }
    return render(request, "index.html", context)
