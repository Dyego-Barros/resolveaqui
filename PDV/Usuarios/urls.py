from django.urls import path
from .views.view_usuario import Usuario

urlpatterns =[
    path("cadastrar", Usuario.as_view(), name="cadastraUsuario"),
    path("", Usuario.as_view(), name="loginUsuario"),
    path("logout", Usuario.as_view(), name="logout")
]