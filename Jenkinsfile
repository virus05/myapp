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

        stage('Trivy FS Scan') {
            steps {
                sh """
                    echo "Running Trivy filesystem scan on workspace..."

                    trivy fs \
                        --severity HIGH,CRITICAL \
                        --format json \
                        --output trivy-fs-report.json \
                        .

                    trivy fs \
                        --severity HIGH,CRITICAL \
                        --exit-code 1 \
                        --no-progress \
                        .
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'trivy-fs-report.json', allowEmptyArchive: true
            echo "Pipeline finished."
        }
        success {
            echo "Deployment + security scan successful."
        }
        failure {
            echo "Pipeline failed (build/deploy/scan). Check logs."
        }
    }
}
