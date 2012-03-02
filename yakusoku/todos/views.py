# coding=utf-8

# Python
from datetime import date, datetime

# Plugins
from annoying.decorators import render_to

# Django
from django.shortcuts import redirect

# Project
from members.models import Pair, Member
from todos.models import Todo


@render_to('todo.html')
def handler(request, slug = ''):
    # cp viewing pair
    # mp login member pair
    # m login member
    # m1 left member
    # m2 right member
    # l m == m1
    # r m == m2
    # h cp == mp
    
    mid = request.session.get('mid', default = None)
    if mid is not None:
        m = Member.objects.get(pk = mid)
        mp = m.pair
    else:
        m = None
        mp = None
    
    if (slug == ''):
        if (m):
            return redirect('/' + m.pair.slug)
        else:
            return redirect('/example')
    
    r = Pair.objects.filter(slug = slug.lower())
    if (r.count() == 0):
        return redirect('/example')
    
    today = date.today()
    
    cp = r[0]
    if cp.member_set.all()[0].isleft:
        m1 = cp.member_set.all()[0]
        m2 = cp.member_set.all()[1]
    else:
        m1 = cp.member_set.all()[1]
        m2 = cp.member_set.all()[0]
    
    for x in (m1, m2):
        x.today_todo = []
        x.old_todo = []
        x.old_done = []
        today_count = 0
        today_done = 0
        for q in x.todo_set.all():
            if (q.created.date() == today):
                x.today_todo.append(q)
                today_count += 1
                if (q.done):
                    today_done += 1
            else:
                if (q.done):
                    x.old_done.append(q)
                else:
                    x.old_todo.append(q)
        if (today_count == 0):
            x.ratio = 0
        else:
            x.ratio = today_done * 100 / today_count
    
    h = False
    l = False
    r = False
    
    if (cp == mp):
        h = True
        if (m1 == m):
            l = True
        else:
            r = True
    
    if (cp.public or ((not cp.public) and (cp == mp))):
        return {'cp' : cp, 'mp' : mp, 'm' : m, 'm1' : m1, 'm2' : m2, 'h' : h, 'l' : l, 'r' : r}
    else:
        return redirect('/m/login')
    
def add(request):
    mid = request.session.get('mid', default = None)
    if mid is not None:
        m = Member.objects.get(pk = mid)
        Todo.objects.create(note = request.POST['note'], owner = m)
        return redirect('/' + m.pair.slug)
    else:
        return redirect('/m/login')

def done(request, tid):
    mid = request.session.get('mid', default = None)
    if mid is not None:
        m = Member.objects.get(pk = mid)
        t = Todo.objects.get(pk = tid)
        if ((t.owner.pair == m.pair) and (t.owner != m)):
            t.done = datetime.now()
            t.save()
            return redirect('/' + m.pair.slug)
    return redirect('/m/login')

def remove(request, tid):
    mid = request.session.get('mid', default = None)
    if mid is not None:
        m = Member.objects.get(pk = mid)
        t = Todo.objects.get(pk = tid)
        if (t.owner == m):
            t.delete()
            return redirect('/' + m.pair.slug)
    return redirect('/m/login')