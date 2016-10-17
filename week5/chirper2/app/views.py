from django.shortcuts import render
from app.models import Chirp, Vote
from app.forms import ChirpForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def about_view(request):
    print("sup" + "="*20)
    message = request.GET.get("message", "")
    return render(request, "about.html")



class ChirpView(ListView):
    template_name = "chirps.html"
    model = Chirp

class ChirpDetailView(DetailView):
    model = Chirp

class ChirpCreateView(CreateView):
    model = Chirp
    success_url = "/chirps"
    fields = ('body', )

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class ChirpUpdateView(UpdateView):
    model = Chirp
    success_url = "/chirps"
    fields = ('body', )

class UserCreateView(CreateView):
    model = User
    success_url = "/chirps" #show reverse_lazy
    form_class = UserCreationForm

class ChirpVoteView(CreateView):
    model = Vote
    fields = ('user','chirp','value')
    success_url = "/chirps"
    def form_valid(self, form):
        try:
            vote.objects.get(user=self.request.user, chirp_id=self.kwargs["pk"]).delete()
        except Vote.DoesNotExist:
            pass
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.chirp = Chirp.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
