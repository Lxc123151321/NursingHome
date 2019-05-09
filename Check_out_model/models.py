from django.db import models
# Create your models here.

class Check_out(models.Model):

    # 主键
    customerID = models.CharField(primary_key=True, max_length=12)
    # 退住类型，原因，时间，状态（是否审核），时间，备注。
    check_out_type = models.CharField(max_length=20)
    check_out_reason =  models.TextField()
    check_out_time =  models.DateField()
    check_out_state =  models.BooleanField()
    time =  models.DateField()
    remark =  models.TextField()