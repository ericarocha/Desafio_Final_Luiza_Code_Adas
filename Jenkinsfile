pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: 
[], userRemoteConfigs: [[credentialsId: '4afadf64-547f-4a5a-ad13-1ee718153e0d', url: 'https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas.git']]])
            }
        }

        stage('Build') {
            steps {
                git branch: 'main', credentialsId: '4afadf64-547f-4a5a-ad13-1ee718153e0d', url: 'https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas.git'
            }
        }

        stage('Test') {
            steps {
                git credentialsId: '4afadf64-547f-4a5a-ad13-1ee718153e0d', 
url: 'https://github.com/ericarocha/Desafio_Final_Luiza_Code_Adas.git'
                echo 'The job finish'
            }
        }
    }
}
