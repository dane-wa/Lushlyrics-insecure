from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import playlist_user
from django.urls.base import reverse
from django.contrib.auth import authenticate,login,logout
from youtube_search import YoutubeSearch
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages



f = open('card.json', 'r')
CONTAINER = json.load(f)

def default(request):
    global CONTAINER


    if request.method == 'POST':

        add_playlist(request)
        return HttpResponse("")

    song = 'kSFJGEHDCrQ'
    return render(request, 'player.html',{'CONTAINER':CONTAINER, 'song':song})


@login_required()
def playlist(request):
    cur_user, created = playlist_user.objects.get_or_create(username=request.user)
    try:
        song = request.GET.get('song')
        song = cur_user.playlist_song_set.get(song_title=song)
        song.delete()
    except:
        pass
    if request.method == 'POST':
        add_playlist(request)
        return HttpResponse("")
    song = 'kSFJGEHDCrQ'
    user_playlist = cur_user.playlist_song_set.all()
    # print(list(playlist_row)[0].song_title)
    return render(request, 'playlist.html', {'song':song,'user_playlist':user_playlist})


def search(request):
    if request.method == 'POST':

        add_playlist(request)
        return HttpResponse("")
    try:
        search = request.GET.get('search')
        song = YoutubeSearch(search, max_results=10).to_dict()
        song_li = [song[:10:2],song[1:10:2]]
        # print(song_li)
    except:
        return redirect('/')

    return render(request, 'search.html', {'CONTAINER': song_li, 'song':song_li[0][0]['id']})



@login_required
def add_playlist(request):
    cur_user = playlist_user.objects.get(username = request.user)

    if (request.POST['title'],) not in cur_user.playlist_song_set.values_list('song_title', ):

        songdic = (YoutubeSearch(request.POST['title'], max_results=1).to_dict())[0]
        song__albumsrc=songdic['thumbnails'][0]
        cur_user.playlist_song_set.create(song_title=request.POST['title'],song_dur=request.POST['duration'],
        song_albumsrc = song__albumsrc,
        song_channel=request.POST['channel'], song_date_added=request.POST['date'],song_youtube_id=request.POST['songid'])


def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        # Vérification que tous les champs sont remplis
        if not all([firstName, lastName, email, password, confirmPassword]):
            messages.error(request, 'Tous les champs sont obligatoires.')
            return render(request, 'signup.html')

        # Vérification des mots de passe
        if password != confirmPassword:
            messages.error(request,'Les mots de passe ne correspondent pas.')
            return render(request, 'signup.html')

        # Vérification si un utilisateur avec cet email existe déjà
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Un utilisateur avec cet email existe déjà.')
            return render(request, 'signup.html')

        # Création de l'utilisateur
        try:
            my_user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            my_user.first_name = firstName
            my_user.last_name = lastName
            my_user.save()
        except Exception as e:
            messages.error(request,  f' Erreur lors de la création du compte : {e}')
            return render(request, 'signup.html')

        messages.success(request, 'Votre compte a été créé avec succès.')
        return redirect('login')

    return render(request, 'signup.html')

def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        if not email or not password:
            messages.error(request, "Tous les champs sont obligatoires.")
            return render(request, 'login.html', {'email': email})

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('default')
        else:
            messages.error(request, 'Identifiants invalides. Vérifiez votre email et mot de passe.')
            return render(request, 'login.html', {'email': email})

    return render(request, 'login.html', {})

def logoutView(request):
    logout(request)
    return redirect('default')

