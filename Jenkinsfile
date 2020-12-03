pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    when {
	    branch 'main'
    }
    stages {
        stage ('Test'){
            steps {
                echo 'when ${BRANCH_NAME}'
            }
        }
    }
}
