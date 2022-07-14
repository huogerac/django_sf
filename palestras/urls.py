from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_eventos, name='palestras.pagina.eventos'),
    path('votacao', views.pagina_votacao, name='palestras.pagina.votacao'),
    path('votacao/poc2', views.pagina_votacao_poc2, name='palestras.pagina.votacao.poc2'),
    path('votacao/concluida', views.pagina_concluida, name='palestras.pagina.votacao.concluida'),
]
