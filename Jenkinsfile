pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }

    stages {
        stage ('Test'){
		when {
			branch BRANCH_NAME
		}
		steps {
                	echo 'when ${BRANCH_NAME}'
            	}
        }
    }
}
