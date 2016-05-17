import json
import urllib
from django.contrib.auth import logout, authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template import RequestContext
import requests
from parkowanie.forms import RegisterForm, LoginForm
from parkowanie.models import News, Park, RegisterModel
from django.utils import timezone
from django.contrib.auth.models import User


def main_page(request):
    Users = User.objects.all()
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'parkowanie/template/parkowanie/main_page.html', {'news': news})


def contact_page(request):
    return render(request, 'parkowanie/template/parkowanie/contact_page.html', {})


def park_page(request):
    urll = 'https://polar-plains-14145.herokuapp.com/parks'
    wp = urllib.request.urlopen(urll).read().decode('utf8')
    pw = json.loads(wp)

    return render(request, 'parkowanie/template/parkowanie/park_page.html', {'parks': pw})


def logout_page(request):
    logout(request)
    return redirect('main_page')


def login_page(request):
    if request.method == "POST":
        form = LoginForm()
        if form.is_valid():
            post = form.save(commit=False)
            url = 'https://polar-plains-14145.herokuapp.com/login'
            data = urllib.parse.urlencode({'login': post.login, 'password': post.password}).encode('utf-8')
            req = urllib.request.urlopen(url, data).read().decode('utf-8')

            return redirect('main_page')
    else:
        form = LoginForm()
    return render(request, 'parkowanie/template/parkowanie/login.html', {'form': form})


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            try:
                send_mail(
                    request.POST['subject'],
                    request.POST['message'],
                    request.POST.get('email', 'support@ruunalbe.com'),
                    ['siteowner@example.com'],
                )
                return HttpResponse('Dziękujemy!')
            except Exception as err:
                return HttpResponse(str(err))
    return render(request, 'parkowanie/template/parkowanie/contact_page.html',
                  {'errors': errors})


def register_page(request):
    # todo zrobic walidacje i wyeliminowac nulle
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['passw'],
                email=form.cleaned_data['email']
            )

            url = 'https://polar-plains-14145.herokuapp.com/users/add'
            data = {'login': form.cleaned_data['login'], 'password': form.cleaned_data['passw'],
                    'email': form.cleaned_data['email'], 'name': form.cleaned_data['name'],
                    'surname': form.cleaned_data['surname']}
            # req = urllib.request.urlopen(url, data).read().decode('utf-8')

            res = requests.post(url, json=data)
            print(res.status_code)

            # # user.last_name = form.cleaned_data['phone']
            user.save()
            # if form.cleaned_data['log_on']:
            #     user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            #     login(request,user)
            #     template = get_template("parkowanie/template/parkowanie/main_page.html")
            #     variables = RequestContext(request,{'user':user})
            #     output = template.render(variables)
            #     return render(request, 'parkowanie/template/parkowanie/main_page.html', {'user':user})
            # else:
            #     template = get_template("registration/register_success.html")
            #     variables = RequestContext(request,{'username':form.cleaned_data['username']})
            #     output = template.render(variables)
        return render(request, 'parkowanie/template/parkowanie/register.html', {'username': form.cleaned_data['login']})
    # else:
    form = RegisterForm()
    template = get_template("parkowanie/template/parkowanie/register.html")
    variables = RequestContext(request, {'form': form})
    output = template.render(variables)
    return render(request, 'parkowanie/template/parkowanie/register.html', {'form': form})
