from django.urls import path
from .views.view_login import Login
from .views.view_cadastro_usuario import Usuario
from .views.view_listar_usuario import listarUsuario
from .views.view_excluir_usuario import ExcluirUsuario
from .views.view_desativar_usuario import DesativarUsuario
urlpatterns =[   
    path("", Login.as_view(), name="loginUsuario"),
    path("logout", Login.as_view(), name="logout"),
    path("cadastrar", Usuario.as_view(), name="cadastrarUsuario"),
    path("listar", listarUsuario.as_view(), name="listarUsuario"),
    path("editar", listarUsuario.as_view(), name="editarUsuario"),
    path("excluir", ExcluirUsuario.as_view(), name="excluirUsuario"),
    path("desativar", DesativarUsuario.as_view(), name="desativarUsuario")
]