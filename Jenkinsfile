pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    stages {
        stage ('Test'){
            steps {
                echo $env.BRANCH_NAME
            }
        }
    }
}
