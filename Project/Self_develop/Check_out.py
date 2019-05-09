import datetime
import random
from TestModel.models import *
from Check_out_model.models import  *

class Check_out(object):

    customerID = ''
    check_out_type = ''
    check_out_reason = ''
    check_out_time = ''
    remark = ''

    time = ''
    check_out_state = False

    def __init__(self,customerID, check_out_type, check_out_reason,check_out_time,remark):

        self.customerID = customerID
        self.check_out_type = check_out_type
        self.check_out_reason = check_out_reason
        self.check_out_time = check_out_time
        self.remark = remark

        # 自动生成办理时间
        self.time = datetime.date.today().strftime('%Y-%m-%d')
        self.check_out_state = False