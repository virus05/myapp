pipeline {
    agent any

    stages {

        stage('init') {
            steps {
                sh """
                    echo "Cleaning old containers..."
                    docker compose down || true

                    echo "Creating network if missing..."
                    docker network create myapp_net || true

                    echo "Ensuring volumes exist..."
                    docker volume create myapp_data || true
                """
            }
        }

        stage('build') {
            steps {
                sh """
                    echo "Building Docker image..."
                    docker build -t myapp:latest .
                """
            }
        }

        stage('deploy') {
            steps {
                sh """
                    echo "Starting containers..."
                    docker compose up -d --force-recreate
                """
            }
        }
    }

    post {
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Deployment failed!"
        }
        always {
            echo "Pipeline finished."
        }
    }
}
