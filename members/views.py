# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> hello </h1>")

def test(req):
    return HttpResponse("<h2> Test </h2>")

def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        
        member = Members(
                username = username,
                useremail = email
        )
        
        member.save()

        res_data = {}
        res_data['res'] = '등록성공'

        return render(req, 'index.html', res_data)

    return render(req, 'index.html')
