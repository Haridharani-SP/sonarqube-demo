pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-pipeline') {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=sonar-demo \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://localhost:9000 \
                    -Dsonar.login=squ_c4f3e6b02b895b3e0e62d6c354879192fe63c977
                    '''
                }
            }
        }
    }
}
