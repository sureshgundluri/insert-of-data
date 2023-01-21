from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter topic:')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()

    return HttpResponse('topic insert successfully')

def insert_webpage(request):
    tn=input('enter topic:')
    name=input('enter name:')
    url=input('enter url:')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()

    return HttpResponse('webpage inserted successfully')

def insert_access(request):
    tn=input('enter topic:')
    name=input('enter name:')
    url=input('enter url:')
    date=input('enter date:')

    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    A=Access_records.objects.get_or_create(name=W,date=date)[0]
    A.save()

    return HttpResponse('Accessrecords are inserted successfully')






