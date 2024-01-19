# Trong views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import secrets
from .models import OtpVendor

def generateToken():
    """
    Sinh một token ngẫu nhiên với độ dài 64 ký tự.
    """
    return secrets.token_urlsafe(64)

def save_token(request):
    if request.method == 'POST':
        # Xử lý sinh token
        generated_token = generateToken()

        # Lấy id của OtpVendor từ yêu cầu (tuỳ thuộc vào cách bạn chuyển id từ frontend)
        otp_vendor_id = request.POST.get('otp_vendor_id')

        # Lấy đối tượng OtpVendor cần được cập nhật
        otp_vendor = get_object_or_404(OtpVendor, pk=otp_vendor_id)

        # Gán token cho trường LinkToken
        otp_vendor.linktoken = generated_token

        # Lưu trạng thái mới của đối tượng
        otp_vendor.save()

        return JsonResponse({'status': 'success', 'message': 'Token đã được lưu thành công!'})

    return JsonResponse({'status': 'error', 'message': 'Yêu cầu không hợp lệ!'})


