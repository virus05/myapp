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
				sh """
					python3 -m venv venv
					. venv/bin/activate
					pip install -r requirements.txt
				"""
			}
		}
                stage('Run app.py') {
                        steps {
                                sh "python3 app.py"
                        }
                }
        }

}
