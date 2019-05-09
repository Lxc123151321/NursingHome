from django.http import HttpResponse
from django.shortcuts import render

"""
    测试文件 第一步
"""

# def hello(request):
#     return HttpResponse("Hello world ! ")

def hello(request):
    context = {}
    context['hello'] = 'Hello World! For mother russia!'
    return render(request, 'hello.html',context)

