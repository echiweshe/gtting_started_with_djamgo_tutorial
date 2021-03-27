from django.urls import path
from .views import (
    descriptivestats_create_view, 
    descriptivestats_detail_view, 
    descriptivestats_delete_view,
    descriptivestats_list_view,
    descriptivestats_update_view,
    
)

app_name = 'descriptivestats'
urlpatterns = [
    path('', descriptivestats_list_view, name='descriptivestats-list'),
    path('create/', descriptivestats_create_view, name='descriptivestats-list'),
    path('<int:id>/', descriptivestats_detail_view, name='descriptivestats-detail'),
    path('<int:id>/update/', descriptivestats_update_view, name='descriptivestats-update'),
    path('<int:id>/delete/', descriptivestats_delete_view, name='descriptivestats-delete'),
]