from django.shortcuts import render
from django.views.decorators import csrf
from Project.Self_develop import Customer
# 接收POST请求数据
def add(request):
    if request.POST:
        name = request.POST['name']
        ctx['sex'] = request.POST['sex']
        ctx['age'] = request.POST['age']
        ctx['nation'] = request.POST['nation']
        ctx['birthdate'] = request.POST['birthdate']

    return

def search():
    return
def modify():
    return
def delete():
    return

