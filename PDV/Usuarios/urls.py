from django.urls import path
from .views.view_login import Login
from .views.view_cadastro_usuario import Usuario
from .views.view_listar_usuario import listarUsuario
urlpatterns =[   
    path("", Login.as_view(), name="loginUsuario"),
    path("logout", Login.as_view(), name="logout"),
    path("cadastrar", Usuario.as_view(), name="cadastrarUsuario"),
    path("listar", listarUsuario.as_view(), name="listarUsuario"),
    path("editar", listarUsuario.as_view(), name="editarUsuario")
]