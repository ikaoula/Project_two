from django.shortcuts import render
from django.http import HttpResponse

from app_two.models import *
# Create your views here.

def index(request):
    users = CustomUser.objects.all()
    my_data = {'users': users}
    return render(request, 'app_two/index.html', context=my_data)
