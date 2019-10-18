from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World')

def sobreView(request):
    return HttpResponse('Opa, tudo beleza!')

def viadoView(request):
    return HttpResponse('Venho informar que as pessoas <b> Eduardo Alves Cuzcuz</b> e <b> Kauan Yuri Cornao</b> são os mais cornos possíveis, além de serem viados')