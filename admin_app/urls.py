from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard', views.admin_dashboard_view, name='admin_dashboard'),
    path('sellerverification/<int:id>/',views.seller_verification,name='sellerverification'),
    path('productverification/<int:id>/', views.product_verification, name='productverification'),
    
    # Attribute Management APIs
    path('api/create-attribute/', views.create_attribute, name='create_attribute'),
    path('api/create-attribute-option/', views.create_attribute_option, name='create_attribute_option'),
    
    # Verification APIs
    path('api/verify-seller/', views.verify_seller_ajax, name='verify_seller_ajax'),
    path('api/verify-product/', views.verify_product_ajax, name='verify_product_ajax'),
]
