from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    space_4 = '&nbsp;' * 4
    return HttpResponse("Hello Word!<br>" + space_4 + "Это мой первый проект на Django!")
