node {
    deleteDir()

    try {      
        stage('Checkout') {
            checkout([
                $class: 'GitSCM', branches: [[name: "${params.branch}"]], doGenerateSubmoduleConfigurations: false,
                extensions: [[$class: 'CloneOption', depth: 1, noTags: true, reference: '', shallow: true,parentCredentials: false,]],
                userRemoteConfigs: [[url: 'https://github.com/KisialiouAliaksei/airflow-dags.git']]
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
