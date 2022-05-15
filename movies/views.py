from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from datetime import datetime
from .models import Movie

# Create your views here.

def index(request):
    return render(request, "index.html")


def movie_list(request):
    movies_from_db = Movie.objects.all()
    context = {
        "movies": movies_from_db,
        "date": datetime.now()
    }
    return render(request, "movie_list.html", context)


def profile_view(request):
    return render(request, "profile.html")


def user_signup(request):
    if request.method == "POST":
        # sprawdzanie poprawności danych, tworzenie użytkownika
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "registration/signup_complete.html")
    else:
        # wyśletlamy pusty formularz
        form = UserCreationForm()

    return render(request, "registration/signup_form.html", context={"form": form})
