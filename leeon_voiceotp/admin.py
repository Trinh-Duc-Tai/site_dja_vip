from django.contrib import admin
from .models import OptTopup, OtpCallPartner202312, OtpCallPartner202401, OtpCallVendor202312, OtpCallVendor202401, OtpPartner, OtpVendor, PrefixTelco, Tmp
from django.utils.translation import gettext as _
from django.utils.html import format_html
from django import forms
import random
from django.utils.safestring import mark_safe

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
    formatted_created_at.admin_order_field = 'createdtime'
    

# @admin.register(OtpCallPartner202312)
class OtpCallPartner202312Admin(NoDeletePermissionAdmin,NoAddPermissionAdmin, BaseAdminWithHiddenButtons):
    # list_display = ['id', 'phone', 'sms', 'responseid', 'formatted_created_at', 'result', 'status', 'hangupcausecode', 'hangupcausedesc', 'billsec', 'duration', 'answersec', 'partnerid', 'partnerresponsecode', 'partnerresponsedesc']
    list_display = ['id', 'phone', 'sms', 'formatted_created_at', 'result', 'status', 'billsec', 'partnerid', 'partnerresponsedesc']
    list_per_page = 23
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')
    formatted_created_at.admin_order_field = 'createdtime'

# @admin.register(OtpCallPartner202401)
class OtpCallPartner202401Admin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    # list_display = ['id', 'phone', 'sms', 'responseid', 'formatted_created_at', 'result', 'status', 'hangupcausecode', 'hangupcausedesc', 'billsec', 'duration', 'answersec', 'partnerid', 'partnerresponsecode', 'partnerresponsedesc']
    list_display = ['id', 'phone', 'sms', 'formatted_created_at', 'result', 'status', 'billsec', 'partnerid', 'partnerresponsedesc']
    list_per_page = 23
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')
    formatted_created_at.admin_order_field = 'createdtime'

# @admin.register(OtpCallVendor202312)
class OtpCallVendor202312Admin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['id', 'phone', 'sms', 'requestid', 'partnerid', 'ip', 'typeof', 'vendorid', 'price', 'status', 'vendorreponsecode', 'vendorreponseid', 'vendorreponsedesc', 'partnerotpprice', 'formatted_created_at']
    list_per_page = 23
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')
    formatted_created_at.admin_order_field = 'createdtime'

# @admin.register(OtpCallVendor202401)
class OtpCallVendor202401Admin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['id', 'phone', 'sms', 'requestid', 'partnerid', 'ip', 'typeof', 'vendorid', 'price', 'status', 'vendorreponsecode', 'vendorreponseid', 'vendorreponsedesc', 'partnerotpprice', 'formatted_created_at']
    list_per_page = 23
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')
    formatted_created_at.admin_order_field = 'createdtime'

def generate_token():
    length = 20
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(charset) for _ in range(length))
class OtpPartnerForm(forms.ModelForm):
    class Meta:
        model = OtpPartner
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Thiết lập widget cho trường vendorid
        self.fields['vendorid'].widget = forms.Select(choices=[(vendor.id, f'{vendor.id} - {vendor.accountname}') for vendor in OtpVendor.objects.all()])
        self.fields['ssecretkey'].widget.attrs['style'] = 'width: 800px;border: None;outline:none'
        self.fields['linkcallback'].widget.attrs['style'] = 'width: 500px;'
        if not self.instance.pk:    
            self.fields['ssecretkey'].initial = generate_token()
            self.fields['ssecretkey'].widget.attrs['readonly'] = True
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
    vendor_account_name.admin_order_field = 'vendorid'

    def display_status(self, obj):
        if obj.status == 0:
            return format_html('<span style="color: red;">&#10007;</span>')  # Đỏ, ví dụ là biểu tượng X
        elif obj.status == 1:
            return format_html('<span style="color: #4caf50;width=20px; font-weight:bold">&#10003;</span>')  # Xanh, ví dụ là biểu tượng tích
        else:
            # return format_html('<span style="color: black;">-</span>') 
            return obj.status  # Nếu giá trị không phải 0 hoặc 1, hiển thị giá trị đó
    display_status.short_description = 'Trạng thái'
    display_status.admin_order_field = 'status'

    def display_limitbalance(self, obj):
        try:
            limitbalance_value = float(obj.limitbalance)
        except ValueError:
            return obj.limitbalance  # Trả về giá trị ban đầu nếu không thể chuyển đổi
        formatted_limitbalance = "{:,.0f}".format(limitbalance_value)
        return formatted_limitbalance

    display_limitbalance.short_description = 'Hạn mức'
    display_limitbalance.admin_order_field = 'limitbalance'

    def display_currentbalance(self, obj):
        try:
            currentbalance_value = float(obj.currentbalance)
        except ValueError:
            return obj.currentbalance  # Trả về giá trị ban đầu nếu không thể chuyển đổi
        formatted_currentbalance = "{:,.2f}".format(currentbalance_value)
        return formatted_currentbalance
    display_currentbalance.short_description = 'Hạn mức sử dụng'
    display_currentbalance.admin_order_field = 'currentbalance'

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
        self.fields['linktoken'].widget.attrs['style'] = 'width: 800px;'
        # if not self.instance.pk:    
            # Nếu là màn hình add, tự động sinh token và hiển thị
            # self.fields['linktoken'].initial = generate_token()
            # self.fields['linktoken'].widget.attrs['readonly'] = True
        # self.fields['linkbody'].widget.attrs['style'] = 'width: 500px;'
        # self.fields['accountname'].widget.attrs['style'] = 'width: 500px;'
from django.utils.html import escape, format_html
@admin.register(OtpVendor)
class OtpVendorAdmin(NoDeletePermissionAdmin,BaseAdminWithHiddenButtons):
    # list_display = ['accountname', 'linkapi', 'linkbody', 'linktoken']
    list_display = ['accountname', 'linkapi', 'linkbody_tooltip', 'linktoken']
    list_per_page = 23
    fields = ['linkapi', 'accountname', 'linkbody', 'linktoken']
    form=OtpVendorForm
    # readonly_fields = ('linktoken',)
    def linkbody_tooltip(self, obj):
        max_length = 50

        if obj.linkbody:
            tooltip_content = escape(obj.linkbody)
            if len(obj.linkbody) > max_length:
                linkbody_value = f'{obj.linkbody[:max_length]}...'
                print("nana", linkbody_value)
            else:
                linkbody_value = obj.linkbody
            return mark_safe(format_html('<span class="sortable" data-toggle="tooltip" data-placement="top" title="{}" data-original-title="{}">{}</span>', tooltip_content, tooltip_content, linkbody_value))
        else:
            return obj.linkbody
    linkbody_tooltip.short_description = "Link Body"
    linkbody_tooltip.admin_order_field = 'linkbody'

@admin.register(PrefixTelco)
class PrefixTelcoAdmin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['prefix', 'telco', 'khienhd', 'mtcvoiceotp', 'miltech', 'frs', 'number_3tech', 'number_1zvietnam', 'fts', 'tel4vn', 'imedia', 'bluelink']
    list_per_page = 23

@admin.register(Tmp)
class TmpAdmin(NoDeletePermissionAdmin,NoAddPermissionAdmin,BaseAdminWithHiddenButtons):
    list_display = ['id', 'createdtime', 'transactionid', 'status', 'account', 'password']
    list_per_page = 23


# -----------------
from .models import OtpCallPartner, OtpCallVendor
from rangefilter.filters import (
    DateRangeFilterBuilder,
)
class OtpCallPartnerAdmin(BaseAdminWithHiddenButtons,NoDeletePermissionAdmin,NoAddPermissionAdmin):
    list_display = [ 'phone', 'sms', 'status','formatted_created_at', 'result', 'billsec', 'partner_account_name']
    # Điều chỉnh hiển thị và truy cập các trường của model tạm thời
    list_per_page = 23
    list_filter = (
        ('createdtime',DateRangeFilterBuilder(title=_('Lọc theo thời gian'))),
    ) 
    search_fields = ('phone','billsec')
    def partner_account_name(self, obj):
        if obj.partnerid:
            partner = OtpPartner.objects.get(pk=obj.partnerid)
            return partner.accountname
        return None
    partner_account_name.short_description = 'Khách hàng'
    partner_account_name.admin_order_field = 'partnerid'
    # date_hierarchy = 'createdtime'
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')
    formatted_created_at.admin_order_field = 'createdtime'
    def get_queryset(self, request):
        # queryset_202312 = OtpCallPartner202312.objects.all()
        # queryset_202401 = OtpCallPartner202401.objects.all()
        # # Thực hiện logic tích hợp dữ liệu từ cả hai bảng
        # queryset = queryset_202312.union(queryset_202401)
        queryset = OtpCallPartner202312.objects.all()
        if OtpCallPartner202401.objects.exists():
            queryset = queryset.union(OtpCallPartner202401.objects.all())
        return queryset
admin.site.register(OtpCallPartner, OtpCallPartnerAdmin)

class OtpCallVendorAdmin(BaseAdminWithHiddenButtons,NoDeletePermissionAdmin,NoAddPermissionAdmin):
    # list_display = ['id', 'phone', 'sms', 'requestid', 'partnerid', 'ip', 'typeof', 'vendorid', 'price', 'status', 'vendorreponsecode', 'vendorreponseid', 'vendorreponsedesc', 'partnerotpprice', 'formatted_created_at']
    list_display = [ 'id','phone', 'sms', 'requestid', 'partner_account_name', 'ip', 'typeof', 'price', 'status', 'vendorreponseid', 'vendorreponsedesc', 'formatted_created_at']
    list_per_page = 23
    list_filter = (
        ('createdtime',DateRangeFilterBuilder(title=_('Lọc theo thời gian'))),
    ) 
    search_fields = ('phone','status')
    # date_hierarchy = 'createdtime'
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.createdtime).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created_Time')
    formatted_created_at.admin_order_field = 'createdtime'
    def partner_account_name(self, obj):
        if obj.partnerid:
            partner = OtpPartner.objects.get(pk=obj.partnerid)
            return partner.accountname
        return None
    partner_account_name.short_description = _('Khách hàng')
    partner_account_name.admin_order_field = "partnerid"
    def get_queryset(self, request):
        queryset = OtpCallVendor202312.objects.all()
        if OtpCallVendor202401.objects.exists():
            queryset = queryset.union(OtpCallVendor202401.objects.all())
        return queryset
admin.site.register(OtpCallVendor, OtpCallVendorAdmin)