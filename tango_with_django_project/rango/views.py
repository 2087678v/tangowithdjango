from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("I says hey there world! <a href='/rango/about'>About</a>")
def about(request):
	return HttpResponse ("This tutorial has been put together by Ivan Valkov, 2087678v <a href='/rango/'>Index</a>")
