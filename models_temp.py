from django.db import models


class OptTopup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId', blank=True, null=True)  # Field name made lowercase.
    topup = models.CharField(db_column='Topup', max_length=20, blank=True, null=True)  # Field name made lowercase.
    currentbalance = models.CharField(db_column='CurrentBalance', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='UpdatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opt_topup'
        verbose_name_plural="OptTopup"


class OtpCallPartner202312(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sms = models.CharField(db_column='Sms', max_length=10, blank=True, null=True)  # Field name made lowercase.
    responseid = models.CharField(db_column='ResponseId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hangupcausecode = models.IntegerField(db_column='HangupCauseCode', blank=True, null=True)  # Field name made lowercase.
    hangupcausedesc = models.CharField(db_column='HangupCauseDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billsec = models.IntegerField(db_column='BillSec', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    answersec = models.IntegerField(db_column='AnswerSec', blank=True, null=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId', blank=True, null=True)  # Field name made lowercase.
    partnerresponsecode = models.CharField(db_column='PartnerResponseCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    partnerresponsedesc = models.CharField(db_column='PartnerResponseDesc', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otp_call_partner_202312'
        verbose_name_plural="OtpCallPartner202312"


class OtpCallPartner202401(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sms = models.CharField(db_column='Sms', max_length=10, blank=True, null=True)  # Field name made lowercase.
    responseid = models.CharField(db_column='ResponseId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hangupcausecode = models.IntegerField(db_column='HangupCauseCode', blank=True, null=True)  # Field name made lowercase.
    hangupcausedesc = models.CharField(db_column='HangupCauseDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billsec = models.IntegerField(db_column='BillSec', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    answersec = models.IntegerField(db_column='AnswerSec', blank=True, null=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId', blank=True, null=True)  # Field name made lowercase.
    partnerresponsecode = models.CharField(db_column='PartnerResponseCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    partnerresponsedesc = models.CharField(db_column='PartnerResponseDesc', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otp_call_partner_202401'
        verbose_name_plural = "OtpCallPartner202401"


class OtpCallVendor202312(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sms = models.CharField(db_column='Sms', max_length=10, blank=True, null=True)  # Field name made lowercase.
    requestid = models.CharField(db_column='RequestId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typeof = models.IntegerField(db_column='Typeof', blank=True, null=True)  # Field name made lowercase.
    vendorid = models.IntegerField(db_column='VendorId', blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    vendorreponsecode = models.IntegerField(db_column='VendorReponseCode', blank=True, null=True)  # Field name made lowercase.
    vendorreponseid = models.CharField(db_column='VendorReponseId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendorreponsedesc = models.CharField(db_column='VendorReponseDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    partnerotpprice = models.CharField(db_column='PartnerOtpPrice', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otp_call_vendor_202312'
        verbose_name_plural = "OtpCallVendor202312"


class OtpCallVendor202401(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sms = models.CharField(db_column='Sms', max_length=10, blank=True, null=True)  # Field name made lowercase.
    requestid = models.CharField(db_column='RequestId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typeof = models.IntegerField(db_column='Typeof', blank=True, null=True)  # Field name made lowercase.
    vendorid = models.IntegerField(db_column='VendorId', blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    vendorreponsecode = models.IntegerField(db_column='VendorReponseCode', blank=True, null=True)  # Field name made lowercase.
    vendorreponseid = models.CharField(db_column='VendorReponseId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendorreponsedesc = models.CharField(db_column='VendorReponseDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    partnerotpprice = models.CharField(db_column='PartnerOtpPrice', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otp_call_vendor_202401'
        verbose_name_plural = "OtpCallVendor202401"


class OtpPartner(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=200, db_collation='utf8mb3_unicode_ci', blank=True, null=True, verbose_name="Khách hàng")  # Field name made lowercase.
    sourcenumber = models.IntegerField(db_column='SourceNumber', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=200, db_collation='utf8mb3_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    ssecretkey = models.CharField(db_column='SsecretKey', max_length=200, db_collation='latin1_swedish_ci', blank=True, null=True, verbose_name="Token")  # Field name made lowercase.
    STATUS_CHOICES = [
        # (0, '0'),
        # (1, '1'),
        (0, 'Chưa hoạt động'),
        (1, 'Đang hoạt động'),
        (None, 'Không xác định'),
    ]
    def default_status_value():
        default_status = OtpPartner.objects.get(pk=1).status
        return default_status
    status = models.IntegerField(db_column='Status', default=0,blank=True, null=True, verbose_name="Trạng thái",choices=STATUS_CHOICES)  # Field name made lowercase.
    # status = models.IntegerField(db_column='Status', default=0,blank=True, null=True, verbose_name="Trạng thái")  # Field name made lowercase.
    linkcallback = models.CharField(db_column='LinkCallBack', max_length=200, blank=True, null=True,verbose_name="Link Callback")  # Field name made lowercase.
    linkbody = models.TextField(db_column='LinkBody', blank=True, null=True,verbose_name="Body")  # Field name made lowercase.
    vendorid = models.IntegerField(db_column='VendorId', blank=True, null=True)  # Field name made lowercase.
    limitbalance = models.CharField(db_column='LimitBalance', max_length=20, blank=True, null=True,verbose_name="Hạn mức")  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=10, blank=True, null=True,verbose_name="Giá")  # Field name made lowercase.
    currentbalance = models.CharField(db_column='CurrentBalance', max_length=20, blank=True, null=True,verbose_name="Hạn mức sử dụng")  # Field name made lowercase.
    todayconsumption = models.CharField(db_column='TodayConsumption', max_length=20, blank=True, null=True)  # Field name made lowercase.
    typemoney = models.IntegerField(db_column='TypeMoney', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'otp_partner'
        verbose_name_plural = "OtpPartner"

import random
import string
def generateToken():
    length = 64
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~'
    return ''.join(random.choice(charset) for _ in range(length))

class OtpVendor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=200, db_collation='utf8mb3_unicode_ci', blank=True, null=True, verbose_name="Nhà cung cấp")  # Field name made lowercase.
    linkapi = models.CharField(db_column='LinkApi', max_length=200, db_collation='utf8mb3_unicode_ci', blank=True, null=True, verbose_name="Link API")  # Field name made lowercase.
    linkbody = models.TextField(db_column='LinkBody', db_collation='utf8mb3_unicode_ci', blank=True, null=True, verbose_name="Body")  # Field name made lowercase.
    linktoken = models.CharField(db_column='LinkToken', max_length=200, blank=True, null=True, verbose_name="Token")  # Field name made lowercase.

    def save(self, *args, **kwargs):
        # Sinh token nếu trường linktoken không có giá trị
        if not self.linktoken:
            self.linktoken = generateToken()
        super().save(*args, **kwargs)
    class Meta:
        managed = False
        db_table = 'otp_vendor'
        verbose_name_plural = "OtpVendor"


class PrefixTelco(models.Model):
    prefix = models.CharField(max_length=10, blank=True, null=True)
    telco = models.CharField(max_length=50, blank=True, null=True)
    khienhd = models.CharField(max_length=20, blank=True, null=True)
    mtcvoiceotp = models.CharField(max_length=20, blank=True, null=True)
    miltech = models.CharField(max_length=20, blank=True, null=True)
    frs = models.CharField(max_length=20, blank=True, null=True)
    number_3tech = models.CharField(db_column='3tech', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1zvietnam = models.CharField(db_column='1zvietnam', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    fts = models.CharField(max_length=20, blank=True, null=True)
    tel4vn = models.CharField(max_length=20, blank=True, null=True)
    imedia = models.CharField(max_length=5, blank=True, null=True)
    bluelink = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prefix_telco'
        verbose_name_plural = "PrefixTelco"


class Tmp(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TransactionId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=10, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp'
        verbose_name_plural = "Tmp"

