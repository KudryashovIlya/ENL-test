pipeline {
    agent {
        docker { image 'python:3.8' }
    }
    parametres {
    	string(defaultValue: '', description: 'Run small flow', name: 'SmallFlow')
    }
    stages {
        stage ('Test'){
		steps {
                	script {
				if (!params.SmallFlow.isEmpty()){
					sh 'echo ${params.SmallFlow} >> test.txt'
				} else {
					sh 'echo SmallFlow is empty'
				}

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
