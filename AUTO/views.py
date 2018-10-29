#coding:utf-8
from django.shortcuts import render,HttpResponse,render_to_response
import requests
# Create your views here.


def Index(request):
    return render_to_response('Index.html')




def Login(request):
    return HttpResponse('Hello World')