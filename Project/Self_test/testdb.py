from django.http import HttpResponse

from Project.Self_test.Customer_test import *
from django.db.models import  Q
from TestModel.models import *


class testdb(object):
    @staticmethod
    # 新增客户信息
    def add_test(Customer_info_test):
        c = Customer_info_test
        t1 = TestCustomer(name = c.name,sex = c.sex, nation = c.nation, check_in_date = c.check_in_date,
                          customerID = c.customerID)
        t1.save()
        return True

    @staticmethod
    # 简单查询客户信息
    def search_test1(dic1):
        q = Q()
        # if 'state1' in dic:
        #     q = q&Q(state1 = dic['state1'])
        # if 'state2' in dic:
        #     q = q&Q(state2 = dic['state2'])
        # if 'name' in dic:
        #     q = q&Q(name = dic['name'])
        # if 'nation' in dic:
        #     q = q&Q(nation = dic['nation'])
        if 'sex' in dic1:
            q = q&Q(sex = dic1['sex'])

        customer_list1 = TestCustomer.objects.filter(q)
        print(customer_list1)

        return customer_list1

    @staticmethod
    # 查看客户详细信息
    def search_test3(dic3):
        q1=Q()
        q2 = Q()
        q3 = Q()
        q4 = Q()
        #基本信息
        if 'customerID' in dic3:
            q1 = q1&Q(customerID = dic3['customerID'])

        customer_list3 = TestCustomer.objects.filter(q1)
        #床位信息
        # if customer_list3['bedID']:
        #     q2 = q2&Q(customer_list3['bedID'])
        # #### 预留一条查询信息，查询床位的
        # #护工信息
        # if customer_list3['nurseID']:
        #     q3 = q3&Q(customer_list3['nurseID'])
        # #套餐信息
        # if customer_list3['serviceID']:
        #     q4 = q4&Q(customer_list3['serviceID'])
        return customer_list3

    @staticmethod
    def remove_test(customerID):
        p0 = TestCustomer.objects.filter(customerID=customerID)
        p0.delete()


    @staticmethod
    def modify_test(dict):
        print(dict)
        p0 = TestCustomer.objects.get(customerID = dict['customerID'])
        p0.name = dict['name']
        p0.sex = dict['sex']
        p0.nation = dict['nation']
        p0.save()
        print(p0)

        return True

