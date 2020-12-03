pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    stages {
        stage ('Test'){
            steps {
                script {
                    sh 'echo Hello world and ${env.BRANCH_NAME}'
                }
            }
        }
    }
}
