"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.InscricaoList.as_view(), name='alternativas'),
    path('nome', views.get_name),
    path('realiza_inscricao', views.realiza_inscricao, name='realiza_inscricao'),
    path('<int:pk>', views.InscricaoDetail.as_view(), name='InscricaoDetail'),
    path('alternativa/<int:pk>', views.AlternativaDetail.as_view(), name='alternativa'),
    path('participante/<int:pk>', views.ParticipanteDetail.as_view(), name='participante'),

    #path('', views.IndexView.as_view(), name='index'),
]
