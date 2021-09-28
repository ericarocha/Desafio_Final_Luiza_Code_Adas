# Projeto_LuizaCode - Time Adas

## Sobre o projeto

O projeto apresentado é o desafio final proposto pelo **LuizaCode 4º Edição** e tem como objetivo criar um aplicativo utilizando métodos e ferramentas orientados pela cultura DevOps. 

A aplicação consiste em um MarketPlace de produtos voltados para diversos segmentos: eletrodomésticos, cosméticos, supermercado, informática e vestuário.

Para elaboração do aplicativo foram utilizadas a linguagens Python e SQL, a biblioteca SQLite3, IDE VS Code, Frameworks Django e BootStrap, o servidor Jenkins para automação do App, o Docker para conteinerização e Kubernetes para orquestração dos containers. 

O desafio foi desenvolvido pelas 4 mulheres do Time Adas sendo cada uma responsável pela execução das várias etapas de estruturação do projeto.


### Desenvolvido por:

- [Elisangela Eleutério](https://github.com/elisangelaeleuterio)
- [Érica Rocha](https://github.com/ericarocha)
- [Larissa Monteiro](https://github.com/LcsMonteiro)
- [Valéria Alves Ferreira](https://github.com/ValFerreiraAlv)

### Entregas ###

- README do projeto explicando como configurar o ambiente e rodar o projeto.
- Deploy da aplicação em Kubernetes
- Front-end da aplicação
-  Testes integração.


>  API contendo os seguintes endpoints:

- Listar produtos
- Listar empresas
- Cadastrar produto e empresa
- Adicionar um produto na lista da empresa;
- Remover um produto da lista da empresa; 
- Consultar todos os produtos e empresas cadastradas.

### Instruções para configurar o ambiente e rodar o projeto:

### Antes de Começar

### 1 - ***Crie um fork do projeto:***

> Crie um fork desse projeto e para isso siga o [tutorial de como realizar um fork](https://docs.github.com/pt/github/getting-started-with-github/quickstart/fork-a-repo);
> Após feito o fork, clone o [repositório](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas.git) em seu computador.
 
 ### 2 - ***Ative a máquina virtual do projeto***
Comando para windows

    Desafio_Final_Luiza_Code_Adas/projeto_final_adas/Scripts/activate
    
 ### Inicialize a aplicação

> Abra a pasta clonada do projeto através de sua IDE. 

> Execute o camando para iniciar a aplicação: 

    python.manage.py.runserver

### 1 - ***Acessando a aplicação***

>No navegador acesse:

    http://127.0.0.1:8000/

 ### 2 -  ***Build no Jenkins***

Instale o Jenkins - [Manual](https://www.jenkins.io/doc/book/installing/) 
   
   ###### Obs: Nós iniciamos o Jeakins pelo Docker por meio do comando ######

    docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11 

   > Inicialize o Jenkins

   > Crie uma pipeline referenciando o projeto [Desafio_Final_Luiza_Code_Adas](https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas.git).  
   O Jeankins irá acessar o arquivo Jenkinsfile e criar a Pipeline. 

  ### 3 -  ***Deploy usando Kubernetes*** 

  Execute os comandos:

    minikube start 

    kubectl apply -f deployment.yaml

    minukube dashboard
