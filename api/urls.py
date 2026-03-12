"""
API URL Configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    # CRUD endpoints
    path('items/', views.get_all_items, name='get_all_items'),
    path('items/create/', views.create_item, name='create_item'),
    path('items/<int:item_id>/', views.get_item, name='get_item'),
    path('items/<int:item_id>/update/', views.update_item, name='update_item'),
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    
    # Save items to file
    path('save/', views.save_items, name='save_items'),
    
    # External API call example
    path('external/', views.external_api_call, name='external_api_call'),
]
