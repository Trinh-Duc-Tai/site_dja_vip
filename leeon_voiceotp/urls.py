from django.urls import path

from django.shortcuts import redirect

def redirect_to_admin(request):
    return redirect('admin:index')
urlpatterns = [
    # path('admin-redirect/', redirect_to_admin, name='redirect_to_admin'),
]