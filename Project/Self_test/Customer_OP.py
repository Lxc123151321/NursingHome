


from Project.Self_test.testdb import *
from django.shortcuts import render
from django.http import HttpResponse
from Project.Self_test.Customer_test import *


# 与网页上的按钮一一对应，相当于响应函数

# 手工增加
def add_test(request):

    if request.POST:
        #对传来的信息进行包装，包装成customer对象。 后期可以改进，参数为 name = reque.POST['name']
        c = Customer_info_test(request.POST['name'],request.POST['sex'],request.POST['nation'])
        testdb.add_test(c)
        return HttpResponse('添加成功！！！')
    if request.GET:
        return render(request, "add_info_test.html")


# 文件增加   还未实现
def add_test1(request):
    if request.Post:
        return

# 简单条件查询  已实现
def search_test1(request):
    ctx = {}
    # 查询信息包装为字典
    customer_search1_dict = dict()
    if request.POST:
        if request.POST.get('condition1')!='':
            state = request.POST.get('condition1')
            if state == '在院' or '外出':
                customer_search1_dict['state1'] = state
            if state == '退住':
                customer_search1_dict['state2'] = state
        if request.POST.get('condition2')!='' and request.POST.get('info')!='':
            attr = request.POST.get('condition2')
            customer_search1_dict[attr] = request.POST.get('info')

    #抛给testdb中的函数去查询处理
    ctx['customer_list'] = testdb.search_test1(customer_search1_dict)
    return render(request, 'info_test.html', ctx)

# 复杂条件查询 还未实现
def search_test2(request):
    ctx = {}
    customer_search2_dict = dict()
    if request.POST:
        customer_search2_dict = dict()


# 查看详细信息 已实现
def search_test3(request):
    ctx = {}
    customer_search3_dict = dict()
    #print("到这里了！") 测试
    if request.POST:
        if request.POST.get('customerID'):
            customer_search3_dict['customerID'] = request.POST.get('customerID')

    #print(customer_search3_dict) 测试

    ctx['customer_list'] = testdb.search_test3(customer_search3_dict)

    print('该返回了！')
    return render(request, 'customer_info_display_test.html',ctx)


# 单个删除，customerID 已实现
def remove_test1(request):

    if request.POST:
        if request.POST.get('customerID'):
            testdb.remove_test(request.POST.get('customerID'))

    print(request.POST.get('customerID'))
    return HttpResponse('删除成功！！！')

# 批量删除, customerID：[ID列表],还未实现
def remove_test2(request):
    customer_delete_set = set()
    if request.POST:
        if request.POST.get('customerID'):
            customer_delete_set = request.POST.get('customerID')

    print('接收到4月份枪毙名单啦！')
    print(request.POST.get('customerID'))

    return HttpResponse('删除成功！！！')



# 单个修改第一步
def modify_test(request):
    ctx = {}
    customer_search3_dict = dict()
    #print("到这里了！") 测试
    if request.POST:
        if request.POST.get('customerID'):
            customer_search3_dict['customerID'] = request.POST.get('customerID')

    ctx['customer_list'] = testdb.search_test3(customer_search3_dict)
    return render(request, 'customer_info_modify_test.html',ctx)

# 单个修改第二步
def modify_test1(request):
    customer_modify_dict = dict()
    if request.POST:
        # print(request.POST)
        customer_modify_dict.update(request.POST)
        for i in request.POST.keys():
            print(i,request.POST[i])
            customer_modify_dict[i] = request.POST[i]
        # 测试一下 POST的内容
        del customer_modify_dict['csrfmiddlewaretoken']
        for i in customer_modify_dict.keys():
            print(i,customer_modify_dict[i])

    testdb.modify_test(customer_modify_dict)

    return HttpResponse('修改成功！！！')


# 批量修改 未实现

