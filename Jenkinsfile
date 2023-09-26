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
                echo 'Build ${env.JOB_NAME}...'
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
                sh 'mkdir logs && touch logging.log'
                sh 'echo DB_NAME=$DB_NAME > .env'
                sh 'echo DB_USER=$DB_USER >> .env'
                sh 'echo DB_PASSWORD=$DB_PASSWORD >> .env'
                sh 'echo DB_HOST=$DB_HOST >> .env'
                sh 'echo DB_PORT=$DB_PORT >> .env'
                sh 'echo DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY >> .env'
                sh 'echo DJANGO_DEBUG=$DJANGO_DEBUG >> .env'
                sh 'echo DISABLE_LOGGING=$DISABLE_LOGGING >> .env'
                sh 'echo DATABASE_ENGINE=$DATABASE_ENGINE >> .env'
                sh 'echo DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS >> .env'
                sh 'sudo docker-compose -f docker-compose.yml up -d --build'
            }
        }

    }

}