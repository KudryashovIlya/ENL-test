pipeline {
    agent {
        docker { image 'python:3.8' }
    }
	
    parameters {
	choice(choices:
        '''oblt-desktop\noblt-mobile\nobcom-desktop\nobcom-mobile\nlaimzlv-desktop\nlaimzlv-mobile
        oblv-desktop\noblv-mobile\nmychance-desktop\nmychance-mobile\nobee-desktop\nobee-mobile
        obse-desktop\nobse-mobile\nbestpoker-desktop\nbestpoker-mobile''', description: 'Select', name: 'Brand')
        booleanParam(defaultValue: false, description: 'Check this box if you want to test your PR', name: 'IsTestRun')
    }	
    stages {
        stage('Test'){
		      when {
            anyOf {
              branch 'jenkins-test'
	      expression { params.IsTestRun }
            }
          }
		      steps {
			      sh "BRAND_STR=`echo ${params.Brand} | tr a-z A-Z`"
          }
       }
    }
}
