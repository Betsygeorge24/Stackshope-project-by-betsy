from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard', views.admin_dashboard_view, name='admin_dashboard'),
    path('sellerverification/<int:id>/',views.seller_verification,name='sellerverification'),
    path('productverification/<int:id>/', views.product_verification, name='productverification'),
    
    # Category/Subcategory Management APIs
    path('api/create-category/', views.create_category, name='create_category'),
    path('api/save-category/', views.save_category, name='save_category'),
    path('api/create-subcategory/', views.create_subcategory, name='create_subcategory'),
    path('api/save-subcategory/', views.save_subcategory, name='save_subcategory'),

    # Category/Subcategory and Banner Management (non-admin namespace to avoid Django admin route conflict)
    path('dashboard/save-category/', views.save_category, name='save_category'),
    path('dashboard/save-subcategory/', views.save_subcategory, name='save_subcategory'),
    path('dashboard/save-banner/', views.save_banner, name='save_banner'),
]