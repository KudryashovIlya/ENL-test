pipeline {
    agent {
        docker { image 'my-python' }
    }
    stages {
        stage ('Test'){
		steps {
                	script {
				sh 'python3 -m unittest tests.py'
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
