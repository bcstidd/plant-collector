from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete', views.PlantDelete.as_view(), name='plants_delete'),        
    path('plants/<int:plant_id>/add_thirsty/', views.add_thirsty, name='add_thirsty'),
    path('plants/<int:plant_id>/assoc_admirer/<int:admirer_id>/', views.assoc_admirer, name='assoc_admirer'),
    path('plantss/<int:plant_id>/disassoc_admirer/<int:admirer_id>/', views.disassoc_admirer, name='disassoc_admirer'),
    path('plants/admirers', views.AdmirerList.as_view(), name='admirers_index'),
    path('admirers/<int:pk>/', views.AdmirerDetail.as_view(), name='admirers_detail'),
    path('admirers/create/', views.AdmirerCreate.as_view(), name='admirers_create'),
    path('admirers/<int:pk>/update/', views.AdmirerUpdate.as_view(), name='admirers_update'),
    path('admirers/<int:pk>/delete/', views.AdmirerDelete.as_view(), name='admirers_delete'),

]
