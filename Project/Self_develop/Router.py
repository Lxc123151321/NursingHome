from django.shortcuts import render

def info(request):
    return render(request, "info.html")

def add_info(request):
    return render(request, "add_info.html")

def search_info(request):
    return render(request, "search_info.html")

def modify_info(request):
    return render(request, "search_info.html")

def delete_info(request):
    return render(request, "search_info.html")


# 返回用户管理的初始界面
def customer_manage_test(request):
    return render(request, "info_test.html")

# 返回退住登记_退住信息查询、处理的初始界面
def check_out_1(request):
    return render(request,"check_out_1.html")
# 返回退住登记_退住办理的初始界面
def check_out_2(request):
    return render(request,"check_out_2.html")
def check_out_21(request):
    return render(request,"check_out_21.html")
def check_out_22(request):
    return render(request,"check_out_22.html")


# 合并交互第一次测试
def jh_test(request):
    return render(request,"test3.html")