import datetime
import random
from Customer_model.models import *

class Customer_info(object):
    #客户所有的信息
    # 新增页面需要展示的信息 17个
    image = ''
    name = ''
    sex = ''
    nation = ''
    ID_number = ''
    birthday = ''                   #也可以根据ID_number生成
    province = ''
    city = ''
    area = ''
    adress = ''
    marriage = ''
    type = ''
    height = ''
    weight = ''
    phoneNum1 = ''
    phoneNum2 = ''
    remark = ''

    # 自动生成的信息  7个
    customerID = ''        # 客户id自动生成
    age = ''
    check_in_date = ''
    state1 = True
    state2 = True
    check_out_date = ''

    bedID = ''             # 床位id选择床位后生成

    def __init__(self, name, sex, age, nation, ID_number,province , city, phoneNum1,address,marriage,type,height,weight,birthday,
                 phoneNum2='未填写',area = '无',remark = '没有填写',
                 ):
        # 各项属性的初始化,必须填的
        self.name = name
        self.sex = sex
        self.age = age
        self.nation = nation
        self.ID_number = ID_number
        self.phoneNum1 = phoneNum1
        self.province = province
        self.city = city
        self.adress =address
        self.marriage = marriage
        self.type = type
        self.height = height
        self.weight = weight
        self.birthdate = datetime.datetime.strptime(birthday, '%Y-%m-%d')

        # 有默认初始化值的，不必须填
        self.phoneNum2 = phoneNum2
        self.area = area
        self.remark = remark

        #自动生成的
        self.check_in_date = datetime.date.today().strftime('%Y-%m-%d')
        self.check_out_date = ''
        self.state1 = True
        self.state2 = True

        #自定义生成一个主键 年+ 月+ 日 + 三位自增
        new_customer_id = ''
        new_customer_id += str(datetime.date.today().year) + str(datetime.date.today().month) + str(datetime.date.today().day)

        # 最后四位随机生成，若有重复则重新生成
        j = 0
        while j == 0:
            i = 0
            num = ''
            while i < 4:
                num += random.choice('0123456789')
                i += 1
            new_customer_id += num
            res = Customer.objects.filter(staffID=new_customer_id)

            if len(res) == 0:
                # 如果在表中没有找到相同的员工id，则该条员工id是有效的
                self.staffID = new_customer_id
                # 系统用户名和员工号是相同的
                j = 1

            else:
                # 否则该条员工id无效，应当重新生成后四位员工id
                new_customer_id -= num
                res.clear()
