# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from .models import user,anime,comment
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'myanimelist/index.html')
def register(request):
    if request.method == 'POST':
        errors =  user.objects.validation(request.POST)
        if 'user' in errors:
            request.session['currentuser']=errors['user']
            
            return redirect('/home')
        else:
            for register,error in errors.iteritems():
                messages.error(request, error, extra_tags=register)
            return redirect('/')
    else:
        return redirect('/')
def login(request):
    loginerrors = user.objects.loginvalidation(request.POST)
    if len(loginerrors):
        for login, error in loginerrors.iteritems():
            messages.error(request,error,extra_tags=login)
            return redirect('/')
    else:
        currentuser=user.objects.get(username=request.POST['username'])
        request.session['currentuser']=currentuser
        return redirect('/home')
def success(request):
    if "currentuser"  in request.session:
        context={
            "user":request.session['currentuser'],
            "mondaylist":anime.objects.filter(day="Monday"),
            "tuesdaylist":anime.objects.filter(day="Tuesday"),
            "wednesdaylist":anime.objects.filter(day="Wednesday"),
            "thursdaylist":anime.objects.filter(day="Thursday"),
            "fridaylist":anime.objects.filter(day="Friday"),
            "saturdaylist":anime.objects.filter(day="Saturday"),
            "sundaylist":anime.objects.filter(day="Sunday"),

        }
        return render(request, 'myanimelist/success.html',context)
    else:
        return redirect('/')
def show(request,id):
    if "currentuser" in request.session:
        context={
            "user":request.session['currentuser'],
            "anime":anime.objects.get(id=id),
            "comment":comment.objects.filter(anime_id=id)
        }
        return render(request,'myanimelist/show.html',context)

def addcommentprocess(request,id):
    comment.objects.create(content=request.POST['comment'],rating=request.POST['rating'],commenter=request.session['currentuser'],anime=anime.objects.get(id=id))
    return redirect('/anime/'+id)

def addwatchlistprocess(request,id):
    this_anime=anime.objects.get(id=id)
    this_user=user.objects.get(name=request.session['currentuser'].name)
    this_anime.followers.add(this_user)
    return redirect('/mywatchlist')
def mywatchlist(request):
    if "currentuser" in request.session:
        showuser=request.session['currentuser']
        context={
            "watchlist":showuser.followed_animes.all(),
        }
        return render(request, 'myanimelist/watchlist.html',context)
    else:
        return redirect('/')
        
def userwatchlist(request,id):
    if "currentuser" in request.session:
        displayuser=user.objects.get(id=id)
        context={
            "user":displayuser,
            "watchlist":displayuser.followed_animes.all()
        }
        return render(request, 'myanimelist/profile.html',context)
    else:
        return redirect('/')
def deletereview(request, id):
    animeid = comment.objects.get(id=id).anime_id
    reviewdel = comment.objects.get(id=id)
    reviewdel.delete()
    return redirect('/anime/%s' % animeid)
def logout(request):
    request.session.clear()
    return redirect('/')

