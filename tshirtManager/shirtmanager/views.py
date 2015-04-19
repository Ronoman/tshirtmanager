from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Team


@login_required
def index(request):
    team_list = Team.objects.all()
    context = {'team_list': team_list}
    return render(request, 'shirtmanager/index.html', context)


def login_view(request):
    context = {}
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('shirtmanager:index'))
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            try:
                email = User.objects.get(email=username)

                user = authenticate(username=email.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse('shirtmanager:index'))
        else:
            messages.error(request, "Invalid credentials, please try again.")

    return render(request, 'shirtmanager/login.html', context)