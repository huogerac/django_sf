from django.shortcuts import render

def pagina_eventos(request):
    context = {
        "eventos": [
            {
                "id": 1,
                "nome": "Python Brasil - Manaus",
                "data": "2022-10-17T08:00:00.463531"
            },
            {
                "id": 2,
                "nome": "Buser Tech - Edição 13",
                "data": "2022-07-15T17:30:00.463531"
            }
        ]
    }
    return render(request, 'palestras/eventos.html', context)

def pagina_votacao(request):
    return render(request, 'palestras/votacao.html')

def pagina_votacao_poc2(request):
    return render(request, 'palestras/votacao_poc2.html')

def pagina_concluida(request):
    return render(request, 'palestras/votacao_concluida.html')