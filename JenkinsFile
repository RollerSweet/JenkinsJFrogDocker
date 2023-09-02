pipeline {
    agent {
        label 'docker-agent1' // Agent that we created
    }
    environment {
        VERSION = '1.2.0'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'python3 /tmp/zip_job.py' // Run zip_job.py
                }
            }
        }
        stage('Publish') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    def serverUrl = 'http://10.100.102.114:8082' // Artifactory IP
                    def username = 'task'
                    def password = 'Aa123456'
                    def repository = "artifactory/generic-local/${env.VERSION}" // Repository name
                    
                    def zipFiles = sh(script: 'ls *.zip', returnStdout: true).trim().split('\n')
                    
                    zipFiles.each { zipFile ->
                        sh "curl -u ${username}:${password} -X PUT ${serverUrl}/${repository}/${zipFile} -T ${zipFile}"
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs() // Cleanup workspace
        }
    }
}
