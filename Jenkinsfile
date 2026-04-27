pipeline {
        agent any
        stages {
                stage('Checkout') {
                        steps {
                                checkout scm
                        }
                }
                stage('Run app.py') {
                        steps {
                                sh "python3 app.py"
                        }
                }
        }

}
