pipeline {
    stage ('Test'){
        when {
            branch '${env.BRANCH_NAME}'
        }
        steps {
                sh 'echo Hello world and ${env.BRANCH_NAME}'
        }
    }
}
