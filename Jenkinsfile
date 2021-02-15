pipeline {
    agent {
        docker { image 'python:3.8' }
    }
	
    parameters {
        booleanParam(defaultValue: false, description: 'Check this box if you want to test your PR', name: 'IsTestRun')
    }
	
    stages {
        stage ('Test'){
		when { anyOf { branch: 'jenkins-test' }}
		steps {
                	script {
				if (!params.SmallFlow.isEmpty()){
					sh 'sleep(10) ; echo "here is ${params.SmallFlow}" >> test.txt'
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
