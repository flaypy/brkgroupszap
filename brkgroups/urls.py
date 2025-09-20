from django.urls import path
from app import views

urlpatterns = [
    # Rota para a página principal que renderiza o HTML no servidor
    path('', views.group_list, name='group_list'),

    # Rota para a API que retorna dados em JSON
    path('api/groups/', views.group_list_api, name='group_list_api'),
]
