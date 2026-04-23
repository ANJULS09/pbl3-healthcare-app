pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = 'anjuls09' 
        APP_NAME = 'healthcare-app'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }
    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ANJULS09/pbl3-healthcare-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_HUB_USER}/${APP_NAME}:${IMAGE_TAG} ."
                    sh "docker build -t ${DOCKER_HUB_USER}/${APP_NAME}:latest ."
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh "echo ${PASS} | docker login -u ${USER} --password-stdin"
                    sh "docker push ${DOCKER_HUB_USER}/${APP_NAME}:${IMAGE_TAG}"
                    sh "docker push ${DOCKER_HUB_USER}/${APP_NAME}:latest"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "sed -i 's|DOCKERHUB_IMAGE_PLACEHOLDER|${DOCKER_HUB_USER}/${APP_NAME}:${IMAGE_TAG}|g' deployment.yaml"
                    sh "kubectl apply -f deployment.yaml --validate=false"
                }
            }
        }
    }
}
