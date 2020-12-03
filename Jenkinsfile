pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    stages {
        stage ('Test'){
        when {
            branch '${env.BRANCH_NAME}'
        }
        steps {
                sh 'echo Hello world and ${env.BRANCH_NAME}'
            }
        }
    }
}
