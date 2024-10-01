from django.urls import path
from . views.view_cadastro import Empresa

urlpatterns=[
    path("cadastro", Empresa.as_view(), name="cadastro" )
]