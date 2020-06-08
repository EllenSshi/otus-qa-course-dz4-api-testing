pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                build 'build_image'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                build 'run_tests'
            }
        }
        stage('Report') {
            steps {
                echo 'Reporting...'
                allure includeProperties: false, jdk: '', results: [[path: 'allure_report']]
            }
        }
    }
}