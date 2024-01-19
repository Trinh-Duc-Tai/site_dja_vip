# site_voiceotp/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class RedirectToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404 and not request.path.startswith('/admin/'):
            # Chuyển hướng về trang gốc nếu đường dẫn không tồn tại và không phải là trang admin
            return redirect(reverse('admin:index'))

        return response
