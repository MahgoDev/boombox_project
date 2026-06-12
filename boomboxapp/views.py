from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def create_account(request):
    return HttpResponse ('Account Created')
