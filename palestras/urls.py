from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_eventos, name='palestras.pagina.eventos'),
    path('votacao/batalha', views.pagina_votacao, name='palestras.pagina.votacao'),
    path('votacao/poc1', views.pagina_votacao_poc1, name='palestras.pagina.votacao.poc1'),
    path('votacao/concluida', views.pagina_concluida, name='palestras.pagina.votacao.concluida'),
]
