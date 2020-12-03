pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }

    stages {
        stage ('Test'){
		when {
			branch 'main'
		}
		steps {
                	echo 'when ${BRANCH_NAME}'
            	}
        }
    }
}
