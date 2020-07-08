node {
    deleteDir()

    try {        
        stage('Test') {
           sh 'python test.py'
        }
    }
    catch(err) {
        currentBuild.result = "FAILURE"
        throw err
    }
    //finally{}
}
