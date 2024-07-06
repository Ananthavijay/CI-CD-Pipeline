pipeline {
   agent any
  
   environment {
       DOCKER_HUB_REPO = "ananthavijay/flask-cred-api"
       CONTAINER_NAME = "flask-cred-api"
       DOCKERHUB_CREDENTIALS=credentials('Dockerhub-Credentials')
   }
  
   stages {
       stage('Checkout') {
           steps {
               checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Ananthavijay/CI-CD-pipeline']]])
           }
       }
       stage('Code Analysis') {
            environment {
                scannerHome = tool 'Sonar-Scanner'
            }
            steps {
                script {
                    withSonarQubeEnv('Sonar-Server') {
                        bat "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=Flask-CRED-API"
                    }
                }
            }
        }
       stage('Build') {
           steps {
               echo "Building.."
               bat "docker image build -t ${DOCKER_HUB_REPO}:latest . --rm"
           }
       }
       stage('Deploy') {
           steps {
               echo "Deploying...."
               bat "docker stop ${CONTAINER_NAME} || (exit 0)"
               bat "docker rm ${CONTAINER_NAME} || (exit 0)"
               bat "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${DOCKER_HUB_REPO}"
           }
       }
      stage('Push') {
           steps {
               echo 'Pushing image..'
               bat "docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW"
               bat "docker push ${DOCKER_HUB_REPO}:latest"
           }
       }
   }
}
