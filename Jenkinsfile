pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    stages {
        stage ('Test'){
            steps {
                sh 'echo Hello world and ${env.BRANCH_NAME}'
            }
        }
    }
}
