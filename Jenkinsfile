pipeline {
    agent any

    stages {

        stage('Deploy') {
            steps {
                sh '''
                docker rm -f myapp || true
                docker pull sahilx987/myapp:latest
                docker run -d -p 5000:5000 --name myapp sahilx987/myapp:latest
                '''
            }
        }
    }
}
