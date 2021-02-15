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
               	 allOf {
                    branch 'production'
                    environment name: 'DEPLOY_TO', value: 'production'
                }
            }
		steps {
			echo '${params.IsTestRun}'
            	}
        }
    }
}
