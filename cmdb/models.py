from django.db import models

# Create your models here.
'''

#这个模块是用来创建数据库的具体表的

'''

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

class Test(models.Model):
    name = models.CharField(max_length=20)

class PhoneInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    phonename = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    version = models.CharField(max_length=32)
    loandate = models.CharField(max_length=32)
    dec = models.CharField(max_length=100)
    os = models.CharField(max_length=32)

# class CardInfo(models.Model):
#     id = models.BigAutoField(primary_key=True) #id
#     cardrule = models.CharField(max_length=32) # 卡制 电信移动联通
#     cardnum = models.CharField(max_length=32)   # 号码
#     username = models.CharField(max_length=32)  # 持有人
#     loandate = models.CharField(max_length=32)  #借用时间
#     active = models.CharField(max_length=32)  #激活人
#     emailuser = models.CharField(max_length=100) # 邮箱账号
#     emailpwd = models.CharField(max_length=100)  # 邮箱密码
#     wecatpwd = models.CharField(max_length=100) # 微信密码
#     wecatpay = models.CharField(max_length=100) # 微信支付密码
#     qquser = models.CharField(max_length=100)  # QQ账号
#     qqpwd = models.CharField(max_length=100)  # QQ密码
#     dec = models.CharField(max_length=100) # 备注
