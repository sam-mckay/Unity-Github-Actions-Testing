pipeline {
  agent any
  stages {
    stage('Unit Test') {
      steps {
        sh '"C:\\Program Files\\Unity\\Hub\\Editor\\2020.3.9f1\\Editor\\Unity.exe" -runTests -batchmode -projectPath $WORKSPACE -testResults $WORKSPACE\\results.xml '
      }
    }

  }
}