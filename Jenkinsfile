pipeline {
   agent any
  
   environment {
       DOCKER_HUB_REPO = "ananthavijay/flask-cred-api"
       CONTAINER_NAME = "flask-cred-api"
 
   }
  
   stages {
       stage('Checkout') {
           steps {
               checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Ananthavijay/CI-CD-pipeline']]])
           }
       }
       stage('Build') {
           steps {
               echo 'Building..'
               sh 'docker image build -t $DOCKER_HUB_REPO:latest .'
           }
       }
       stage('Deploy') {
           steps {
               echo 'Deploying....'
               sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME $DOCKER_HUB_REPO'
           }
       }
   }
}
