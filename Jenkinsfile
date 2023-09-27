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
            }
        }

        stage('Create environment') {
            steps {
                script {
                    def envVars = [
                        'DB_NAME',
                        'DB_USER',
                        'DB_PASSWORD',
                        'DB_HOST',
                        'DB_PORT',
                        'DJANGO_SECRET_KEY',
                        'DJANGO_DEBUG',
                        'DISABLE_LOGGING',
                        'DATABASE_ENGINE',
                        'DJANGO_ALLOWED_HOSTS',
                        'CSRF_TRUSTED_ORIGINS'
                    ]
                    sh 'rm -f .env'
                    envVars.each { envVar ->
                        def credential = credentials(envVar)
                        sh "echo ${envVar}=${credential} >> .env"
                    }
                }
            }
        }

        stage('Deploy application') {
            steps {
                sh 'mkdir logs && touch logging.log'
                sh 'sudo docker-compose -f docker-compose.yml up -d --build'
                sh 'sudo docker cp library_management:/app/static ./static'
            }
        }

        stage('Clear Stopped Containers') {
            steps {
                sh 'sudo docker container prune -f'
            }
        }

        stage('Clear Unused Images') {
            steps {
                sh 'sudo docker rmi $(sudo docker images -f "dangling=true" -q) &>/dev/null'
            }
        }
    }
}