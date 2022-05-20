from django.urls import path
from .views import colaborador_create
from .views import colaborador_read
from .views import colaborador_update
from .views import colaborador_delete

urlpatterns = [
    path('novo/', colaborador_create, name="colaborador_create"),
    path('lista/', colaborador_read, name="colaborador_read"),
    path('editar/<int:id>/', colaborador_update, name="colaborador_update"),
    path('deletar/<int:id>/', colaborador_delete, name="colaborador_delete")
]
