# Guia do desenvolvedor - Django Speaker Fight

## Como rodar o projeto na minha máquina

Olá, Tudo bem?
Este é um guia simples, para te ajudar a rodar um projeto localmente (na sua máquina).

Do que precisamos?
1- um projeto pra rodar
2- uma máquina
3- vontade 

## Passo 1 - Clonando um repositório

Para começar, temos que clonar o repositório do projeto que queremos rodar. 
Clique em "Code" na página deste projeto (no GitHub)
nesse momento, temos duas opções:
  -HTTPS
  -SSH

Mas, quando usar cada uma delas?
   
   ### SSH
   use essa chave se você for um colaborador do projeto, ela dá um acesso enorme! Dá pra fazer git push direto, sem ter que abrir uma issue e ser aprovado, por exemplo.

   ### HTTPS
   use essa chave se você for <s>um pobre camponês</s> qualquer outra pessoa! Você pode fazer alterações locais, mas não vai interferir no projeto real.

Escolheu sua chave? então joga no terminal assim:
     `git clone + chave SSH ou HTTPS`

## Passo 2 - ativando o Django

    caminhe até a pasta do projeto, no caso do speaker fighter:

        `cd django_sf`
    Agora uma parte muito importante: ativar o ambiente virtual

        `virtualenv .venv` 
    (este comando cria um ambiente virtual, utilizar o nome '.venv' vai facilitar sua vida )
    
        `source .venv/bin/activate`

    (este comando ativa o ambiente virtual, para desativar basta escrever "deactivate" no terminal)

### Por que usar um ambiente virtual? a pergunta que não quer calar todo iniciante

            o ambiente virtual serve basicamente para instalar as dependências que seu projeto precisa, sem instalar 
        direto no computador. Suponha que seu projeto_1 use o python 3.8, enquanto o projeto_2 utiliza o python 3.10,
        imagina que trampo ter que instalar e desintalar essas versões cada vez que for mexer neles. 
        
            Ou que seu projeto_1 seja uma calculadora, nele faz sentido importar a biblioteca Math, mas o projeto_2
        seja algo totalmente nada a ver, o ambiente virtual permite instalar só o necessário para cada projeto.
    
## Passo 3 - Instalando as dependências do projeto
    Agora iremos instalar tudo que nosso projetinho precisa pra funcionar, rode o comando abaixo no terminal:
    
    `pip install -r requirements.txt`

    (Não esqueça de ativar seu ambiente virtual, hein!!!!)

    O projeto possui um arquivo chamado requirements.txt que basicamente é um documento listando todas as dependências.
    Estamos falando assim: "olá senhor computador, pode instalar pra mim tudo que esse projeto precisa pra rodar??"

    Mas, como nem tudo são flores, tem um carinha que gosta de dar trabalho pra gente, mas não se assuste! Muitas vezes
    não conseguimos instalar o psycopg2 e isso pode ser a causa do erro (caso tenha dado algum erro, né?)
    digite `pip freeze` no seu terminal e veja se o psycopg2 está instalado!

    se não tiver, lança um `pip install psycopg2`
    provavelmente ele vai reclamar que falta instalar algo, leia o erro pra saber o que é que tá causando essa carência nele! e dê um `apt-get install`

    exemplo: apt-get install libpq-dev python3-dev

## Vamos Rodar esse projeto!!!!
    Por último mas não menos importante, falta rodar o bonito, e lá vamos nós:

    lance o brabo: 
    
    `./manage.py runserver`

    e por fim, `Ctrl + click` no link que o terminal vai te passar!

    Parabéns, Você rodou um projeto !!! esse momento é todo seu S2





