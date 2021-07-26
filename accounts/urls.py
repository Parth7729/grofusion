from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/user/register/', views.register_handler, name="register"),
    path('dashboard/user/otp-verification/', views.otp_handler, name="otp"),
    path('dashboard/user/login/', views.login_handler, name="login"),
    path('dashboard/user/logout/', views.logout_handler, name='logout'),
    path('dashboard/update-profile/seller/', views.update_profile_seller, name='update-profile-seller'),
    path('dashboard/upload-documents/seller/', views.upload_documents_seller, name='upload-documents-seller'),
    path('dashboard/update-profile/buyer/', views.update_profile_buyer, name='update-profile-buyer'),
]
