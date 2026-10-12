pipeline {
  agent any
  environment {
    IMAGE_NAME = 'admininstagram/jenkins-docker-db-app'
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build App') {
      steps {
        bat 'echo Mulai build proyek'
      }
    }
    stage('Build Docker Image') {
      steps {
        bat 'docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
        bat 'docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest'
      }
    }
    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS,
            usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
          bat 'echo %DH_PASS%| docker login -u %DH_USER% --password-stdin'
          bat 'docker push %IMAGE_NAME%:%BUILD_NUMBER%'
          bat 'docker push %IMAGE_NAME%:latest'
        }
      }
    }
    stage('Deploy App + Database') {
      steps {
        bat 'docker compose -p jenkins-demo up -d --build'
      }
    }
  }
  post {
    always {
      echo 'Selesai build'
    }
  }
}