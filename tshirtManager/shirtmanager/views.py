from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Team


@login_required
def index(request):
    team_list = Team.objects.all()
    context = {'team_list': team_list}
    return render(request, 'shirtmanager/index.html', context)

def login(request):
    context = {}
    return render(request, 'shirtmanager/login.html', context)