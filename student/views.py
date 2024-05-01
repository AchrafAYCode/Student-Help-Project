from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect   
from django.contrib.auth.forms import UserCreationForm
from .forms import LogementForm




def index (request) :
    context = {'form' : LogementForm()}
    return render(request,'student/list.html',context)
    
    
    
    
    
    
    
def login(request) :
    if request .method=="POST" :
        form = AuthenticationForm(request .POST)
        if form . is_valid() :
            user_email = form.cleaned_data['email']
            logged_user = User.objects.get(courriel=user_email)
            request.session['logged_user_id'] = logged_user.id
            return redirect ('/home')
        else:
            form = AuthenticationForm()
    return render('student/registration/acceuils.html ' , {'form' : form}) 


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request)
            messages.success(request, f"Coucou {username}, Votre compte a été créé avec succès !")
            return redirect("index")
    else:
        form = UserCreationForm()
    
    return render(request, "student/registration/register.html", {"form": form})

 
def logout_view(request):
    logout(request)


def loading_page(request):
    return render(request, 'loading.html') 



from django.shortcuts import render
from .models import Logement, Stage, Evénement, EvenClub, EvenSocial

def afficher_posts(request):
    logements = Logement.objects.all()
    stages = Stage.objects.all()
    evenements = Evénement.objects.all()
    evenements_club = EvenClub.objects.all()
    evenements_social = EvenSocial.objects.all()

    return render(request, 'afficher_posts.html', {
        'logements': logements,
        'stages': stages,
        'evenements': evenements,
        'evenements_club': evenements_club,
        'evenements_social': evenements_social,
    })