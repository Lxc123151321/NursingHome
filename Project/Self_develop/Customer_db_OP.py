from django.shortcuts import render
from django.views.decorators import csrf
from Project.Self_develop.Customer import Customer_info
from Customer_model.models import Customer

# 接收POST请求数据
def add(request):
    if request.POST:
        customer = Customer_info(name = request.POST['name'], sex= request.POST['sex'], age= request.POST['age'], nation= request.POST['nation'],
                            ID_number= request.POST['ID_number'],province= request.POST['province'] , city= request.POST['province'], phoneNum1= request.POST['phonenum1'],
                            address= request.POST['province'],marriage= request.POST['name'],type= request.POST['name'],height= request.POST['height'],
                            weight= request.POST['height'],birthday= request.POST['birthdate'],phoneNum2=request.POST['phonenum1'],area = request.POST['province'],remark = request.POST['phonenum1'])

    cfo = Customer()


    return


def search():
    return


def modify():
    return


def delete():
    return