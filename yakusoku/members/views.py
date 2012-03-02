# coding=utf-8

# Python
import hashlib

# Plugins
from annoying.decorators import render_to

# Django
from django.shortcuts import redirect

# Project
from members.models import Pair, Member

@render_to('signup.html')
def signup(request):
    if request.method == 'POST':
        error = {}
        if len(request.POST['slug']) < 2:
            error['slug'] = "URL too short, 2-40 is required."
        if len(request.POST['slug']) > 40:
            error['slug'] = "URL too long, 2-40 is required."
        if (Pair.objects.filter(slug=request.POST['slug'].lower()).count() != 0):
            error['slug'] = "URL has been taken."
        if (Member.objects.filter(nick=request.POST['left'].lower()).count() != 0):
            error['nickleft'] = "Nickname has been taken."
        if (Member.objects.filter(nick=request.POST['right'].lower()).count() != 0):
            error['nickright'] = "Nickname has been taken."
        
        if error == {}:
            p = Pair.objects.create(title = request.POST['pairtitle'] ,slug = request.POST['slug'].lower())
            if request.POST.get('public', default = False):
                p.public = True
                p.save()
            m1 = Member.objects.create(nick = request.POST['left'].lower(), password = "temp", isleft = True, pair = p)
            m1.save()
            m2 = Member.objects.create(nick = request.POST['right'].lower(), password = "temp", isleft = False, pair = p)
            m2.save()
            return redirect('/m/login')
        else:
            return {'error' : error}
    else:
        return {}

@render_to('login.html')
def login(request):
    if request.method == "POST":
        error = {}
        
        r = Member.objects.filter(nick = request.POST['nick'].lower())
        
        if (r.count() == 0):
            error['nick'] = "Unknown nickname."
            return {'error' : error}
        else:
            m = r[0]
            
            h = hashlib.md5()
            h.update(request.POST['password'])
            
            if (not m.locked):
                m.locked = True
                m.password = h.hexdigest()
                m.save()
                request.session['mid'] = m.id
                return redirect('/' + m.pair.slug)
            else:
                if (h.hexdigest() == m.password):
                    request.session['mid'] = m.id
                    return redirect('/' + m.pair.slug)
                else:
                    error['password'] = "Wrong password."
                    return {'error' : error}
    else:
        return {}