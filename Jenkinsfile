node {
    deleteDir()

    try {      
        stage('Checkout') {
            checkout([
                $class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false,
                extensions: [[$class: 'CloneOption', depth: 1, noTags: true, reference: '', shallow: true,parentCredentials: false]],
                userRemoteConfigs: [[url: 'https://github.com/KisialiouAliaksei/airflow-dags']]
            ])
        }
        stage('Test') {
           sh 'python --version'
        }
    }
    catch(err) {
        currentBuild.result = "FAILURE"
        throw err
    }
    //finally{}
}
