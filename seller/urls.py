from django.urls import path
from . import views

urlpatterns = [
    path('seller_bridge/', views.seller_bridge, name='seller-bridge'),
    path('becomeseller/',views.seller_broche_view,name="becomeseller"),
    path('seller_bridge/', views.seller_bridge, name='seller-bridge'),
    path('sellerprofile',views.seller_profile_view,name='seller-profile'),
    path("add-product/", views.add_product, name="add-product"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path("manage-variants/<slug:product_slug>/", views.manage_variants, name="manage_variants"),
    path("update-product/<slug:product_slug>/", views.update_product, name="update_product"),
    path("delete-product/<slug:product_slug>/",views.delete_product,name="delete_product"),
    path("seller_customers_orders/", views.seller_customers_orders, name="seller_customers_orders"),
    path('customer_reviews/',views.customer_reviews,name='customer_reviews'),
    path('update-order-status/', views.update_order_status, name='update_order_status'),
    path('seller_analytics/', views.seller_analytics, name='seller_analytics'),
    path('seller-inventory/', views.seller_inventory_view, name='seller_inventory'),
    path('seller-settings/', views.seller_settings_view, name='seller_settings'),
    path("delete-image/<int:image_id>/", views.delete_product_image, name="delete_product_image"),
    path('export-orders/', views.export_orders_csv, name='export_orders_csv'),
]
