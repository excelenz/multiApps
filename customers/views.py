from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def index(request):
    context = {}
    from django.http import HttpResponse
    return HttpResponse('202 ok.', status=202)