from django.shortcuts import render
from Project.Self_test.testdb import *
from django.shortcuts import render
from Project.Self_develop.Check_out_DB_OP import *
from Project.Self_develop.Check_out import *

'''
    测试文件 第二步
'''


def jh_test1(request):
    if request.POST:
        print(request.POST)
    return render(request, 'test3.html')
