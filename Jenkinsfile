pipeline {
        agent any
        stages {
                stage('Checkout') {
                        steps {
                                checkout scm
                        }
                }
		stage('Instal dependencies'){
			steps {
				sh "pip install flask"
			}
		}
                stage('Run app.py') {
                        steps {
                                sh "python3 app.py"
                        }
                }
        }

}
