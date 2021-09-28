# Projeto_LuizaCode - Time Adas


O projeto apresentado é o desafio final proposto pelo **LuizaCode 4º Edição** e tem como objetivo criar um aplicativo utilizando métodos e ferramentas orientados pela cultura DevOps. 

A aplicação consiste em um MarketPlace de produtos voltados para diversos segmentos: eletrodomésticos, cosméticos, supermercado, informática e vestuário.

Para elaboração do aplicativo foram utilizadas a linguagens Python e SQL, a biblioteca SQLite3, IDE VS Code, Frameworks Django e BootStrap, o servidor Jenkins para automação do App, o Docker para conteinerização e Kubernetes para orquestração dos containers. 

O desafio foi desenvolvido pelas 4 mulheres do Time Adas sendo cada uma responsável pela execução das várias etapas de estruturação do projeto.


## Tecnologias que vamos usar:
| Ferramenta | Descrição |
| --- | --- |
| `python` | Linguagem de programação |
| `django` | Ambiente de execução do python|
| `SQLite` | Banco de dados relacional orietado a documentos|
| `MongoDb Compass` | Interface gráfica para verificar se os dados foram persistidos|
 `Insomnia ou Postman` | Interface gráfica para realizar os testes|
|`HTML`|Linguagem de marcação para formatação e organização das páginas|
|`Bootstrap`|Framework front-end que fornece estruturas de CSS para a criação de sites e aplicações responsivas.|
|`Jenkins`|É uma ferramenta de Integração Contínua|
|`Kubernetes`|É uma plataforma open source que faz a automatização das operações dos containers Linux|
|`Docker`|plataforma de código aberto para criação de ambientes isolados via container|
<br>
<br>


#### ENDPOINTS


  **GET**

    -[GET] "/"
    home que retorna a pagina inicial;
    HTTP 200 OK

     -[GET] "/viewseg/:id"
    Para visualizar determinado segmento;
    HTTP 200 OK

     -[GET] "/viewProd/:id"
    Para visualizar determinado produto;
    HTTP 200 OK

     -[GET] "/viewEmpresas/:id"
    Para visualizar determinada empresa;
    HTTP 200 OK

  **POST**

    [POST] "/cdSegmento"
    cdSegmento cria um novo cadastro de segmentos.
    HTTP 201 CREATED

     [POST] "/cd_empresa"
    cd_empresa cria um novo cadastro de empresas.
    HTTP 201 CREATED

     [POST] "/cd_produto"
    cd_produto cria um novo cadastro de produtos.
    HTTP 201 CREATED

**UPDATE**

    [Update] "editseg/:id"
    Edita um segmento.
    HTTP 200 OK

     [Update] "editemp/:id"
    Edita uma empresa.
    HTTP 200 OK

     [Update] "editprod/:id"
    Edita um produto.
    HTTP 200 OK

  **DELETE**

    [Delete] "/deletarEmpresa/:id"
    deletarEmpresa deleta uma empresa.
    HTTP 200 OK

    [Delete] "/deletarProduto/:id"
    deletarProduto deleta um produto.
    HTTP 200 OK

    [Delete] "/deletarSeg/:id"
    deletarSeg deleta um segmento.
    HTTP 200 OK

### Entregas ###

- README do projeto explicando como configurar o ambiente e rodar o projeto.
- Deploy da aplicação em Kubernetes
- Front-end da aplicação
-  Testes integração.

<br>

### Instruções para configurar o ambiente e rodar o projeto:

### Antes de Começar

### 1 - ***Crie um fork do projeto:***

> Crie um fork desse projeto e para isso siga o [tutorial de como realizar um fork](https://docs.github.com/pt/github/getting-started-with-github/quickstart/fork-a-repo);
> Após feito o fork, clone o [repositório](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas.git) em seu computador.

### 2 - ***Clonar o repositório github***
O comando abaixo irá clonar o projeto do Git para dentro do diretório informado. 

    git clone https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas

 
 ## Rodar o servidor sem o docker

 - **Python**  instalado ([Link](https://www.python.org/downloads/));
- **PIP** instalado, é um gerenciador de pacotes do Python.

    Instalar via [Link](https://pypi.org/project/pip/) ou Comandos: 

    ```bash
    curl -O https://bootstrap.pypa.io/pip/3.4/get-pip.py

    sudo -E python3 get-pip.py

    sudo pip install --upgrade pip

    python3 -m pip --version
    ```

- Instalar **Django** ([Link](https://docs.djangoproject.com/pt-br/3.2/topics/install/#installing-official-release))

    Assistam esse vídeo explicando o que é Django depois ([Link](https://www.youtube.com/watch?v=9SUVYuPK2f4&t=4s&ab_channel=CanalPythonProBr))

- Instalar DB Browser para **SQLite** ([Link](https://sqlitebrowser.org/dl/)).

    Vamos usar para melhor visualização Banco de Dados Relacional.

- Instalar **VSCode** ([Link](https://code.visualstudio.com/download))
- Instalar o **Kubernetes** (kubectl) por favor ([Link](https://kubernetes.io/releases/download/))
- Instalar o **Minikube** por favor ([Link](https://minikube.sigs.k8s.io/docs/start/)).
- Opcional. Instalar o **Docker Desktop** ([Link](https://www.docker.com/products/docker-desktop))

<br>


 ### 2 - ***Instale a maquina virtual***
Comando para windows:

    python3 -m pip install virtualenv  


### 3 - ***Inicie a maquina virtual***

    Desafio_Final_Luiza_Code_Adas/projeto_final_adas/Scripts/activate

    
 ### 4  - ***Inicialize a aplicação***

> Entre no caminho que se localiza o arquivo ***manage.py***

> Execute o camando para iniciar a aplicação: 

    python.manage.py.runserver

<br>

## Executar o servidor com o Docker

### 1 - ***Dê o comando abaixo para baixar a imagem***

    docker pull ericarocha/python-crud-adas:v1

### 2 - ***Comando para executar a imagem***

    docker run ericarocha/pyhton-crud-adas:v1



## Acessando a aplicação 

>No navegador acesse:

    http://127.0.0.1:8000/

 ### 2 -  ***Build no Jenkins***

Instale o Jenkins - [Manual](https://www.jenkins.io/doc/book/installing/) 
   
   ###### Obs: Nós iniciamos o Jeakins pelo Docker por meio do comando ######

    docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11 

   > Inicialize o Jenkins

    Acesse localhost:/8080 e insira a senha fornecida no terminal;

   > Crie uma pipeline referenciando o projeto [Desafio_Final_Luiza_Code_Adas](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas.git).  
   O Jeankins irá acessar o arquivo Jenkinsfile e criar a Pipeline.


  ### 3 -  ***Deploy usando Kubernetes*** 

  Execute os comandos:

    minikube start 

    kubectl apply -f deployment.yaml

    minukube dashboard

## Desenvolvido por:

- [Elisangela Eleutério](https://github.com/elisangelaeleuterio)
- [Érica Rocha](https://github.com/ericarocha)
- [Larissa Monteiro](https://github.com/LcsMonteiro)
- [Valéria Alves Ferreira](https://github.com/ValFerreiraAlv)