from random import choices
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
    """
    Deve escolher 2 palestras para deixar o usuário escolher qual é a melhor!
    """
    return render(request, 'palestras/votacao.html')

def pagina_votacao_poc2(request):
    """ cópia da pagina_votacao com um style diferente"""
    autores = [
        {
            "id": 1,
            "nome": "Lu Mastercard",
            "bio": "Lorem ipsum dolor sit and elit Voluptas",
            "imagem": "palestras/imagens/avatar1.png",
        },
        {
            "id": 2,
            "nome": "Enza Pascal",
            "bio": "Lorem ipsum more detail Lups dolor sit and elit Voluptas",
            "imagem": "palestras/imagens/avatar2.png",
        },
        {
            "id": 3,
            "nome": "Pedrão Paulo",
            "bio": "404",
            "imagem": "palestras/imagens/avatar3.png",
        },
        {
            "id": 4,
            "nome": "Liz Laz",
            "bio": "404",
            "imagem": "palestras/imagens/avatar4.png",
        },
    ]
    palestras = [
        {
            "id": 1,
            "titulo": "Api design first",
            "descricao": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas minus vel accusantium enim minima autem, adipisci laboriosam ad inventore?",
            "imagem": "palestras/imagens/palestra1_520x320.png",
            "autor": autores[0],
        },
        {
            "id": 2,
            "titulo": "Deploy de Django no Openshift",
            "descricao": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Corporis ab unde temporibus ipsa suscipit cupiditate. Neque vero perspiciatis numquam explicabo voluptatem fugiat quibusdam.",
            "imagem": "palestras/imagens/palestra2_520x320.png",
            "autor": autores[1],
        },
        {
            "id": 3,
            "titulo": "Django as camadas do futuro!",
            "descricao": "Corporis ab unde temporibus ipsa suscipit cupiditate. Neque vero perspiciatis numquam explicabo voluptatem fugiat quibusdam.",
            "imagem": "palestras/imagens/palestra3_520x320.png",
            "autor": autores[2],
        },
        {
            "id": 4,
            "titulo": "Como não se estressar com Django",
            "descricao": "Adipisicing elit. Corporis ab unde temporibus ipsa suscipit cupiditate. Neque vero perspiciatis numquam explicabo voluptatem fugiat quibusdam.",
            "imagem": "palestras/imagens/palestra4_520x320.png",
            "autor": autores[3],
        },
    ]
    palestra1, palestra2 = choices(palestras, k=2)

    # Não retorna 2 palestras iguais
    if palestra1["id"] == palestra2["id"]:
        for item in palestras:
            if item['id'] != palestra1["id"]:
                palestra1 = item
                break

    context = {
        "palestra1": palestra1,
        "palestra2": palestra2,
    }
    return render(request, 'palestras/votacao_poc2.html', context)

def pagina_concluida(request):
    id_vencedora = request.POST.get("vencedora")
    print("id_vencedora =============> ", id_vencedora)
    return render(request, 'palestras/votacao_concluida.html')
