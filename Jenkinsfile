pipeline {
    agent {
        docker { image 'python:3.8' }
    }
    stages {
        stage ('Test'){
		steps {
                	script {
				sh 'python3 -m unittest main.py /tmp/chromedriver'
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
