node {
    deleteDir()

    try {        
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
