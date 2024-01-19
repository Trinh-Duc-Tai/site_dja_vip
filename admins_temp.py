from django.contrib import admin
from .models import OptTopup, OtpCallPartner202312, OtpCallPartner202401, OtpCallVendor202312, OtpCallVendor202401, OtpPartner, OtpVendor, PrefixTelco, Tmp
from django.utils.translation import gettext as _
from django.utils.html import format_html
from django import forms

admin.site.site_title = "Leeon VoiceOtp VIP"
admin.site.site_header = "VoiceOtp Administration"
admin.site.index_title = "Leeon VoiceOtp Administration"


class BaseAdminWithHiddenButtons(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True  # Ẩn nút "Save"
        extra_context['show_save_and_continue'] = True  # Ẩn nút "Save and continue editing"
        extra_context['show_save_and_add_another'] = False 
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
class NoAddPermissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
class NoDeletePermissionAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(OptTopup)
class OptTopupAdmin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['id', 'partnerid', 'topup', 'currentbalance', 'formatted_created_at', 'updatedtime']
    list_per_page = 23
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')

@admin.register(OtpCallPartner202312)
class OtpCallPartner202312Admin(NoDeletePermissionAdmin,NoAddPermissionAdmin, BaseAdminWithHiddenButtons):
    # list_display = ['id', 'phone', 'sms', 'responseid', 'formatted_created_at', 'result', 'status', 'hangupcausecode', 'hangupcausedesc', 'billsec', 'duration', 'answersec', 'partnerid', 'partnerresponsecode', 'partnerresponsedesc']
    list_display = ['id', 'phone', 'sms', 'formatted_created_at', 'result', 'status', 'billsec', 'partnerid', 'partnerresponsedesc']
    list_per_page = 23
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')

@admin.register(OtpCallPartner202401)
class OtpCallPartner202401Admin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    # list_display = ['id', 'phone', 'sms', 'responseid', 'formatted_created_at', 'result', 'status', 'hangupcausecode', 'hangupcausedesc', 'billsec', 'duration', 'answersec', 'partnerid', 'partnerresponsecode', 'partnerresponsedesc']
    list_display = ['id', 'phone', 'sms', 'formatted_created_at', 'result', 'status', 'billsec', 'partnerid', 'partnerresponsedesc']
    list_per_page = 23
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')

@admin.register(OtpCallVendor202312)
class OtpCallVendor202312Admin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['id', 'phone', 'sms', 'requestid', 'partnerid', 'ip', 'typeof', 'vendorid', 'price', 'status', 'vendorreponsecode', 'vendorreponseid', 'vendorreponsedesc', 'partnerotpprice', 'formatted_created_at']
    list_per_page = 23
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')

@admin.register(OtpCallVendor202401)
class OtpCallVendor202401Admin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['id', 'phone', 'sms', 'requestid', 'partnerid', 'ip', 'typeof', 'vendorid', 'price', 'status', 'vendorreponsecode', 'vendorreponseid', 'vendorreponsedesc', 'partnerotpprice', 'formatted_created_at']
    list_per_page = 23
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')


class OtpPartnerForm(forms.ModelForm):
    class Meta:
        model = OtpPartner
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Thiết lập widget cho trường vendorid
        self.fields['vendorid'].widget = forms.Select(choices=[(vendor.id, f'{vendor.id} - {vendor.accountname}') for vendor in OtpVendor.objects.all()])
        # Điều chỉnh chiều rộng của trường linkcallback
        self.fields['linkcallback'].widget.attrs['style'] = 'width: 500px;'
        # self.fields['vendorid'].widget.attrs['disabled'] = 'disabled' # Ẩn nếu không muốn thay đổi vendorid

@admin.register(OtpPartner)
class OtpPartnerAdmin(NoDeletePermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = [ 'accountname', 'ssecretkey', 'display_status', 'linkcallback', 'vendor_account_name', 'display_limitbalance', 'price', 'display_currentbalance']
    # list_display = [ 'accountname', 'ssecretkey', 'display_status', 'linkcallback', 'vendor_account_name', 'limitbalance', 'price', 'currentbalance']
    # list_display = [ 'accountname', 'ssecretkey', 'status', 'linkcallback', 'vendorid', 'limitbalance', 'price', 'currentbalance']
    list_per_page = 23
    fields = [ 'accountname', 'ssecretkey', 'status', 'linkcallback', 'vendorid', 'limitbalance', 'price', 'currentbalance']
    # readonly_fields = ['accountname','ssecretkey', 'limitbalance', 'price', 'currentbalance']
    form = OtpPartnerForm
    def vendor_account_name(self, obj):
        if obj.vendorid:
            vendor = OtpVendor.objects.get(pk=obj.vendorid)
            return vendor.accountname
        return None
    vendor_account_name.short_description = 'Nhà cung cấp'

    def display_status(self, obj):
        if obj.status == 0:
            return format_html('<span style="color: red;">&#10007;</span>')  # Đỏ, ví dụ là biểu tượng X
        elif obj.status == 1:
            return format_html('<span style="color: #4caf50;width=20px; font-weight:bold">&#10003;</span>')  # Xanh, ví dụ là biểu tượng tích
        else:
            # return format_html('<span style="color: black;">-</span>') 
            return obj.status  # Nếu giá trị không phải 0 hoặc 1, hiển thị giá trị đó
    display_status.short_description = 'Trạng thái'

    def display_limitbalance(self, obj):
        try:
            limitbalance_value = float(obj.limitbalance)
        except ValueError:
            return obj.limitbalance  # Trả về giá trị ban đầu nếu không thể chuyển đổi
        formatted_limitbalance = "{:,.0f}".format(limitbalance_value)
        return formatted_limitbalance

    display_limitbalance.short_description = 'Hạn mức'

    def display_currentbalance(self, obj):
        try:
            currentbalance_value = float(obj.currentbalance)
        except ValueError:
            return obj.currentbalance  # Trả về giá trị ban đầu nếu không thể chuyển đổi
        formatted_currentbalance = "{:,.2f}".format(currentbalance_value)
        return formatted_currentbalance
    display_currentbalance.short_description = 'Hạn mức sử dụng'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('accountname','ssecretkey', 'limitbalance', 'price', 'currentbalance')
        return self.readonly_fields

class OtpVendorForm(forms.ModelForm):
    class Meta:
        model = OtpVendor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Điều chỉnh chiều rộng của trường linkapi
        self.fields['linkapi'].widget.attrs['style'] = 'width: 500px;'

@admin.register(OtpVendor)
class OtpVendorAdmin(NoDeletePermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['accountname', 'linkapi', 'linkbody', 'linktoken']
    list_per_page = 23
    fields = ['linkapi', 'accountname', 'linkbody', 'linktoken']
    readonly_fields = ['linktoken']
    form=OtpVendorForm
    # class Media:
    #     js = ('admin/js/vendor/jquery/jquery.js', 'leeon_voiceotp/js/generate_token.js')

@admin.register(PrefixTelco)
class PrefixTelcoAdmin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['prefix', 'telco', 'khienhd', 'mtcvoiceotp', 'miltech', 'frs', 'number_3tech', 'number_1zvietnam', 'fts', 'tel4vn', 'imedia', 'bluelink']
    list_per_page = 23

@admin.register(Tmp)
class TmpAdmin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['id', 'createdtime', 'transactionid', 'status', 'account', 'password']
    list_per_page = 23


# -----------------
