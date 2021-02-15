pipeline {
    agent {
        docker { image 'python:3.8' }
    }
	
    parameters {
        booleanParam(defaultValue: false, description: 'Check this box if you want to test your PR', name: 'IsTestRun')
    }	
    stages {
        stage('Test'){
		when { 
			branch 'jenkins-test'
		}
		steps {
			echo '${params.IsTestRun}'
            	}
        }
    }
}
