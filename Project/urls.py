"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from django.conf.urls import url
#测试学习
from Project.Self_test import Customer_OP
from Project.learn_test import search2, search, HelloWorld, Hello,jh_test
#正式开发
from Project.Self_develop import CustomerOP,Router,Check_out_OP

urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello/', HelloWorld.hello),
    path('hello1/', Hello.hello),


#学习测试
    url(r'^$', HelloWorld.hello),
   # url(r'^testdb$', testdb.testdb),
    url(r'^search_form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search_post$', search2.search_post),


# 开发正式
    url(r'^info$', Router.info),
    url(r'^add_info$', Router.add_info),
    url(r'^add$', CustomerOP.add),


# 开发测试
    # 整体页面导航
    # 客户管理
    url(r'^customer_manage_test$', Router.customer_manage_test),
    #退住管理
    url(r'^check_out_1$', Router.check_out_1),
    url(r'^check_out_2$', Router.check_out_2),
    url(r'^check_out_21$', Router.check_out_21),
    url(r'^check_out_22$', Router.check_out_22),

    # 客户具体页面导航
    #增加
    url(r'^add_test$', Customer_OP.add_test),
    #查询
    url(r'^search_test1$', Customer_OP.search_test1),
    url(r'^search_test3$', Customer_OP.search_test3),
    #删除
    url(r'^remove_test1$', Customer_OP.remove_test1),
    url(r'^remove_test2$', Customer_OP.remove_test2),
    #修改
    url(r'^modify_test1$', Customer_OP.modify_test1),
    url(r'^modify_test$', Customer_OP.modify_test),

    #退住管理具体页面导航
    #增加
     url(r'^co_add$', Check_out_OP.add1),
    #查询
    url(r'^co_search$', Check_out_OP.search),
    #修改
    url(r'^co_modify1$', Check_out_OP.modify1),
    #url(r'^co_modify2$', Check_out_OP.modify2),
    #删除
    url(r'^co_remove1$', Check_out_OP.remove1),
    #url(r'^co_remove2$', Check_out_OP.remove2),
    # s审核
    url(r'^co_verify1$', Check_out_OP.verify1),
    #url(r'^co_verify2$', Check_out_OP.verify2),


# 合并测试
    url(r'^jh_test', Router.jh_test),
    url(r'^jh_test1', jh_test.jh_test1),

]
