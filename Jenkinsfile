pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    stages {
        stage ('Test'){
            steps {
                echo BRANCH_NAME
            }
        }
    }
}
