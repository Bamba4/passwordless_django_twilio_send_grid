from django.contrib import admin
from django.urls import path
from verification.views import register_page, home_page, login_page, generate_otp, check_otp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_page, name="register"),
    path('check/', check_otp, name="check_otp"),
    path('login/', login_page,  name="login"),
    path('otp/<int:pk>/<uuid>/', generate_otp),
    path('home/', home_page)
]
