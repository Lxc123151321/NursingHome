from Project.Self_test.Customer_test import *
from django.db.models import  Q
from Check_out_model.models import *
from TestModel.models import *

class Check_out_DB_OP(object):
    @staticmethod
    def add(c_o):

        t1 = Check_out(customerID = c_o.customerID, check_out_type = c_o.check_out_type,
                          check_out_reason = c_o.check_out_reason,
                          check_out_time = c_o.time, remark = c_o.remark,
                          time = c_o.time, check_out_state = c_o.check_out_state)
        t1.save()
        return

    @staticmethod
    def search(dict):
        q = Q()

        if 'customerID' in dict:
            q = q&Q(customerID = dict['customerID'])
        if 'check_out_type' in dict:
            q = q&Q(check_out_type = dict['check_out_type'])

        check_out_list = Check_out.objects.filter(q)

        return check_out_list

    @staticmethod
    def remove(customerID):

        p0  = Check_out.objects.get(customerID = customerID)
        p0.delete()

        return True

    @staticmethod
    def modify(dict):
        p0 = Check_out.objects.get(customerID = dict['customerID'])

        p0.check_out_reason = dict['new_check_out_reason']

        p0.save()

        return  True

    @staticmethod
    def verify(customerID):
        p0 = Check_out.objects.get(customerID = customerID)

        p0.check_out_state = True

        p0.save()

        return True