pipeline {
    agent {
        docker { image 'python:3.8' }
    }
    stages {
        stage ('Test'){
		steps {
                	script {
				sh 'echo "Hello" >> test.txt'
			}
            	}
        }
    }
	post {
        	always {
            		archiveArtifacts artifacts: '*.txt', fingerprint: true
        }
    }
}
