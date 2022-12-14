from django.urls import path
from .views import IndexView

urlpatterns = [
    #path('enderoço-da-minha-url/', Minha_view.as_view(), name='nome-da-minha-url'), <- e não esquecer dessa vírgula no final
    path('inicio/', IndexView.as_view(), name='paginaInicial'),
]
