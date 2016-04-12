from django.shortcuts import render
from django.template.loader import get_template
from django.template import RequestContext
from parkowanie.models import News, Park
from django.utils import timezone
from django.contrib.auth.models import User

def main_page(request):
    Users = User.objects.all()
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'parkowanie/template/parkowanie/main_page.html', {'news': news})

def contact_page(request):
    return render(request, 'parkowanie/template/parkowanie/contact_page.html', {})

def park_page(request):
    parks = Park.objects.all()
    return render(request, 'parkowanie/template/parkowanie/park_page.html', {'parks': parks})