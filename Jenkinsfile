pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Build' ${env.JOB_NAME}
            }
        }

        stage('Build') {
            environment {
                DB_NAME=credentials('DB_NAME')
                DB_USER=credentials('DB_USER')
                DB_PASSWORD=credentials('DB_PASSWORD')
                DB_HOST=credentials('DB_HOST')
                DB_PORT=credentials('DB_PORT')
                DJANGO_SECRET_KEY=credentials('DJANGO_SECRET_KEY')
                DJANGO_DEBUG=credentials('DJANGO_DEBUG')
                DISABLE_LOGGING=credentials('DISABLE_LOGGING')
                DATABASE_ENGINE=credentials('DATABASE_ENGINE')
                DJANGO_ALLOWED_HOSTS=credentials('DJANGO_ALLOWED_HOSTS')
            }
            steps {
//                 sh 'cat .env'
                sh 'sudo docker-compose -f docker-compose-prod.yml up -d --build'
            }
        }

    }

}