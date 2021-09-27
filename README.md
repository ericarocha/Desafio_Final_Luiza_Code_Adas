# Projeto_LuizaCode

# Sobre o projeto

O projeto apresentado é o desafio final proposto pelo **LuizaCode 4º Edição** e tem como objetivo criar um aplicativo utilizando métodos e ferramentas orientados pela cultura DevOps. 

A aplicação consiste em um MarketPlace de produtos voltados para diversos segmentos: eletrodomésticos, cosméticos, supermercado, informática e vestuário.

Para elaboração do aplicativo foram utilizadas a linguagens Python e SQL, a biblioteca SQLite3, IDE VS Code, Frameworks Django e BootStrap, o servidor Jenkins para automação do App, o Docker para conteinerização e Kubernetes para orquestração dos containers. 

O desafio foi desenvolvido pelas 4 mulheres do Time Adas sendo cada uma responsável pela execução das várias etapas de estruturação do projeto.

## Layout App

![app](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas/blob/feature/adas-erica/app/apps.py)

![templates](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas/tree/feature/adas-erica/app/Templates)

![migrations](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas/tree/feature/adas-erica/app/migrations)

![forms](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas/blob/feature/adas-erica/app/forms.py)

![models](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas/blob/feature/adas-erica/app/models.py)

![tests](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas/blob/feature/adas-erica/app/tests.py)

![views](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas/blob/feature/adas-erica/app/tests.py)

# Comando
> Criar uma máquina virtual para realizar no PC 
    python -m venv ambiente_virtual 
    
> Ativar a máquina virtual toda vez que a máquina, o comando deve ser repetido. Para isso será necessário ir até a pasta do projeto.
    
    # Em windows
    
    ambiente_virtual\Scripts\activate    
    ambiente_virtual\Scripts\activate.bat
    
    # Unix ou MacOS
    
    source tutorial-env/bin/activate
    
> Instalar DJango no ambiente virtual

    python -m pip install Django
    
> Iniciar uma aplicação devidamente usando Python

    django-admin startproject project .
    
> Iniciar a aplicação com o nome de app

    python manage.py startapp app
    
> Criar um repositório no GITHUB

> Subir as alterações iniciais remotamente:

    git remote add origin https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas
    git branch -M main
    git add .
    git commit -m 'mensagem'
    git push -u origin main

# Codando

> Colocar 'app' no arquivo settings.py dentro de project para o python entender que app faz parte do projeto

> Modificar os arquivos urls e views

> Rodar o server: no terminal logado com a máquina virtual

    python3 manage.py runserver

### Iniciar o layout da aplicação

> Criar a pasta TEMPLATE dentro de APP

> Criar o index.html dentro de template

> Modificar o arquivo views.py

> Copiar e colar o CDN do bootstrap dentro de index.html

> Pesquisar table bootstrap no google

> Mudar a classe padrão thead-dark para table-dark

#### O processo começa com a rota, chama a função que depois renderiza a view desejada

> Criar o form e importá-lo

> Começar nas models                 

> Procurar no google models django

> Mostrar o seguinte link:

    https://docs.djangoproject.com/en/3.2/topics/db/models/#field-types

> Rodar as migrations

    python manage.py makemigrations
    
> Ir na pasta migrations e mostrar

> Criar as tabelas no banco de dados:

    python manage.py migrate
    
> Automaticamente vai no sqlite3. Ir na pasta settings e mostrar o atributo ENGINE

> Abrir o db browser e conectar com banco de dados da app. Inserir o arquivo db.sqlite3

> Criar as models. Link https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/

> Ir nas views e importar a model

> Criar um dicionario chamado data

> form.as_p gera em nome de parágrafo o render da pagina

> No redirect de views, colocar o nome da rota

> Instalando jenkins

    brew install jenkins-lts
    
    brew services start jenkins-lts
    
> Configuração

    sudo nano /usr/local/opt/jenkins-lts/homebrew.mxcl.jenkins-lts.plist
    
> Mudar a linha onde tem o host por 0.0.0.0, como abaixo

    <string>--httpListenAddress=0.0.0.0</string>

> Pegar senha do Jenkins no macos

    sudo cat /Users/mariannesalomaodeoliveira/.jenkins/secrets/initialAdminPassword

> Criar uma tag para a imagem com seu usuario_docker_hub/nome_da_imagem  ou realizar o build e criar a imagem que esse padrão de nome.

    docker build -t django-kube .
    
> Importante tagear a imagem para evitar problema na aplicação

    docker tag django-kube mariannesalomao/django-kube:django-kube
    
> Aplicar o comando docker run

    docker run django-kube

# Kubernetes

> Criar o arquivo deployment.yaml

> Rodar o comando

    minikube start

    kubectl apply -f deployment.yaml

    docker save python-crud | (eval $(minikube docker-env) && docker load)
    
    minikube dashboard (pode dar erro porque o minikube não tem a sua imagem do seu projeto, rodar o comando abaixo)
    
    antes de minikube dashboard, rodar o comando docker save NOMEDASUAAPLICACAO | (eval $(minikube docker-env) && docker load)

# Autoras 

Elisangela Eleuterio 

https://github.com/elisangelaeleuterio

Erica Rocha de Paula Lima 

https://github.com/ericarocha

Larissa Monteiro

https://github.com/LcsMonteiro

Valéria Alves Ferreira 

https://github.com/ValFerreiraAlv

