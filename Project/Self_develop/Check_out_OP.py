from Project.Self_test.testdb import *
from django.shortcuts import render
from Project.Self_develop.Check_out_DB_OP import *
from Project.Self_develop.Check_out import *


# 简单条件查询
def search(request):
    ctx = {}
    check_out_search_dict = dict()
    if request.POST:
        if request.POST.get('customerID')!= '':
            check_out_search_dict['customerID'] = request.POST.get('customerID')
        if request.POST.get('check_out_type')!='':
            check_out_search_dict['check_out_type'] = request.POST.get('check_out_type')

    print(check_out_search_dict)

    ctx['check_out_list'] = Check_out_DB_OP.search(check_out_search_dict)
    return render(request,'check_out_1.html',ctx)

# 手工增加
def add1(request):
    if request.POST:
        # 包装成员一个对象
        c_o = Check_out(customerID=request.POST.get('customerID'),check_out_type=request.POST.get('check_out_type'),
                        check_out_reason=request.POST.get('check_out_reason'),check_out_time=request.POST.get('check_out_time'),
                        remark=request.POST.get('remark'))

        Check_out_DB_OP.add(c_o)
        return HttpResponse('添加成功！！！')

    return render(request,"check_out_21.html")


# 批量增加，可以接受一个excel文件（或者zip文件）来进行处理。待实现
def add2(request):
    # for 循环 包装成对象 c_o
    # Check_out_DB_OP.add(c_o)
    if request.POST:
        return HttpResponse('批量增加处理成功！')
    return render(request,"check_out_22.html")

# 单个修改
def modify1(request):
    print('hello')
    check_out_modify_dict = dict()
    if request.POST:
        check_out_modify_dict.update(request.POST)
        # 打印一下
        for i in request.POST.keys():
            print(i,request.POST[i])
            check_out_modify_dict[i] = request.POST[i]
        # 去掉字典中的特殊key-value
        del check_out_modify_dict['csrfmiddlewaretoken']
        for i in check_out_modify_dict.keys():
            print(i, request.POST[i])

        Check_out_DB_OP.modify(check_out_modify_dict)
        return HttpResponse('修改成功！')

# 批量修改,未实现，取出值循环调用单个修改即可
def modify2(request):
    return HttpResponse('批量修改成功！')

# 单个删除
def remove1(request):
    if request.POST:
        if request.POST.get('customerID'):
            Check_out_DB_OP.remove(request.POST.get('customerID'))
    return HttpResponse('删除成功！')

# 批量删除,未实现，取出值循环调用单个删除即可
def remove2(reqest):
    return HttpResponse('批量删除成功！')
# 单个审核

def verify1(request):
    if request.POST:
        if request.POST.get('customerID'):
            print(request.POST.get('customerID'))
            Check_out_DB_OP.verify(request.POST.get('customerID'))
    return HttpResponse('审核成功！')

# 批量审核，未实现。取出值循环调用单个审核即可
def verify2(request):
    return HttpResponse('批量审核成功！')
