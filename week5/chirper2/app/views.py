from django.shortcuts import render
from app.models import Chirp
from app.forms import ChirpForm
from django.views import View
# Create your views here.

def index_view(request):
    print(request.POST)
    if request.POST:
        instance = ChirpForm(request.POST)
        if instance.is_valid():
            instance.save()
    context = {
        "form": ChirpForm(),
        "all_chirps": Chirp.objects.all().order_by("-created")
    }
    return render(request, "index.html", context)


def about_view(request):
    print("sup" + "="*20)
    message = request.GET.get("message", "")
    return render(request, "about.html")



class ChirpView(View):

    def get(self, request):
        return render(request, "chirps.html")

    def post(self,request):
        return render(request, "chirps.html")
