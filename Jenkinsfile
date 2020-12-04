pipeline {
    agent {
        docker { image 'python:3.8' }
    }
	
    parameters {
	    choice(choices: 'oblt-desktop\noblt-mobile\nobcom-desktop\nobcom-mobile\nlaimzlv-desktop\noblt-desktop.mobile.withdraw', description: 'Select', name: 'Brand')
    	string(defaultValue: '', description: 'Run small flow', name: 'SmallFlow')
    }
	
    stages {
        stage ('Test'){
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
