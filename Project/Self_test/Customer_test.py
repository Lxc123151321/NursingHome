import datetime
import random
from TestModel.models import *

class Customer_info_test(object):

    customerID = ''
    name = ''
    sex = ''
    nation = ''

    check_in_date = ''
    def __init__(self,name, sex, nation):

        self.name = name
        self.nation = nation
        self.sex = sex

        self.check_in_date = datetime.date.today().strftime('%Y-%m-%d')

        # new_customer_id = str(datetime.date.today().year) + str(datetime.date.today().month) + str(
        #     datetime.date.today().day)

        # 生成新的ID
        new_customer_id = datetime.date.today().strftime('%Y-%m-%d').replace('-','')
        j = 0
        while j == 0:
            num = ''
            i = 0
            while i < 4:
                num += random.choice('0123456789')
                i += 1
            new_customer_id += num

            res = TestCustomer.objects.filter(customerID=new_customer_id)
            if len(res) == 0:        # 如果在表中没有找到相同的员工id，则该条员工id是有效的
                j = 1
            else:
                new_customer_id -= num      #反之
                res.clear()
        self.customerID = new_customer_id