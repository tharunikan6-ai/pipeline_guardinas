pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
            }
        }
        stage('Build') {
            steps {
                echo 'Running npm install...'
                // Intentional error: trying to run a package that doesn't exist
                sh 'npm run build-missing-script'
            }
        }
    }
}