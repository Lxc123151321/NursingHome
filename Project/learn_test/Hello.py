from django.http import HttpResponse
from django.shortcuts import render
'''
    测试文件 第二步
'''


def hello(request):
    context = {}
    context['hello'] = 'Hello World! For mother America!'
    return render(request, 'hello.html',context)
