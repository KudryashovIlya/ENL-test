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
               	 anyOf {
                    branch 'jenkins-test'
		    expression { params.IsTestRun }
                }
            }
		steps {
			echo '${params.IsTestRun}'
            	}
        }
    }
}
