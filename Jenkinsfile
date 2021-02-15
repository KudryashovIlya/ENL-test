pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    parameters {
        booleanParam(defaultValue: false, description: 'Check this box if you want to test your PR', name: 'IsTestRun')
    }
    stages {
        stage ('Test'){
            when { anyOf { branch 'master'; params.IsTestRun } }
            steps {
                echo BRANCH_NAME
            }
        }
    }
}
