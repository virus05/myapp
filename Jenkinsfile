pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Init') {
            steps {
                sh """
                    echo "Stopping old containers..."
                    docker compose down || true

                    echo "Creating network if missing..."
                    docker network create myapp_net || true

                    echo "Ensuring volumes exist..."
                    docker volume create myapp_data || true
                """
            }
        }

        stage('Build') {
            steps {
                sh """
                    echo "Building Docker image..."
                    docker build -t myapp:latest .
                """
            }
        }

        stage('Deploy') {
            steps {
                sh """
                    echo "Deploying containers..."
                    docker compose up -d --force-recreate
                """
            }
        }

        stage('Trivy FS Scan') {
            steps {
                sh """
                    echo "Running Trivy filesystem scan..."

                    trivy fs \
                        --severity HIGH,CRITICAL \
                        --format json \
                        --output ${WORKSPACE}/trivy-fs-report.json \
                        ${WORKSPACE}

                    trivy fs \
                        --severity HIGH,CRITICAL \
                        --exit-code 1 \
                        --no-progress \
                        ${WORKSPACE}
                """
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh """
                    echo "Running Trivy image scan..."

                    trivy image \
                        --severity HIGH,CRITICAL \
                        --format json \
                        --output ${WORKSPACE}/trivy-image-report.json \
                        myapp:latest

                    trivy image \
                        --severity HIGH,CRITICAL \
                        --exit-code 1 \
                        --no-progress \
                        myapp:latest
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'trivy-fs-report.json', allowEmptyArchive: true
            archiveArtifacts artifacts: 'trivy-image-report.json', allowEmptyArchive: true
            echo "Pipeline completed."
        }
        success {
            echo "Build, deploy, and security scans successful."
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}
