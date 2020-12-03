pipeline {
    agent {
        docker { image 'python:3.8' }
    }
    stages {
        stage ('Test'){
		when {
			branch BRANCH_NAME
		}
		steps {
                	script {
				sh 'pip3 -r install requirements.txt ; python3 -m unittest main.py'
			}
            	}
        }
    }
	post {
        	always {
            		archiveArtifacts artifacts: 'screenshot/*.png', fingerprint: true
        }
    }
}
