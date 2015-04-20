from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .models import Team, UserProfile


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


def create_account(request):
    context = {}
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('shirtmanager:index'))
    if request.method == "POST":
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "Your passwords did not match.")
            return render(request, 'shirtmanager/register.html')
        team_number = request.POST.get('team')
        username = request.POST.get('username')
        email_address = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            user = User.objects.create_user(username, email_address, password, first_name=first_name, last_name=last_name)
        except IntegrityError as e:
            print(e)
            messages.error(request, "Username has already been taken.")
            return render(request, 'shirtmanager/register.html')

        user.userprofile = UserProfile()

        user.userprofile.team, created = Team.objects.get_or_create(manager_name=username, team_number=team_number)

        user.userprofile.save()

        if created:
            messages.success(request, "Account created successfully, you may now login.")
        return HttpResponseRedirect(reverse("shirtmanager:login"))
    return render(request, 'shirtmanager/register.html')
