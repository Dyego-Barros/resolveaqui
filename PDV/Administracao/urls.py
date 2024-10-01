from django.urls import path
from Administracao.views.view_adm import AdmView


urlpatterns=[
    path("", AdmView.as_view(), name="dashboard")
]


