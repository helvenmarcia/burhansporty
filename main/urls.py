from django.urls import path
from main.views import show_main, add_product, show_product_detail, edit_product, delete_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, proxy_image, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

    path('add-product/', add_product, name='add_product'),
    path('products/<str:id>/', show_product_detail, name='show_product_detail'),
    path('products/<str:id>/edit', edit_product, name='edit_product'),
    path('products/<str:id>/delete', delete_product, name='delete_product'),
    
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('proxy-image/', proxy_image, name='proxy_image'),

    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]

