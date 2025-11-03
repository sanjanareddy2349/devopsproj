pipeline {
    agent any
   
    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"

                // Install Python dependencies
                bat 'pip install -r requirements.txt'

                // ✅ Start Flask app in background
                bat 'start /B python app.py'

                // ⏱️ Wait a few seconds for the server to start
                bat 'ping 127.0.0.1 -n 5 > nul'

                // ✅ Run tests using pytest
                bat 'pytest -v test_pinterestapp.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t pinterestdemo:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                // 🔐 Your Docker Hub credentials
                bat 'docker login -u sanjanaa09 -p Hari@2349'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker image to Docker Hub"
                bat "docker tag pinterestdemo:v1 sanjanaa09/sample:pinterestclone"
                bat "docker push sanjanaa09/sample:pinterestclone"
            }
        }

        stage('Deploy to Kubernetes') { 
            steps { 
                echo "Deploying to Kubernetes"
                bat 'kubectl apply -f deployment.yaml --validate=false' 
                bat 'kubectl apply -f service.yaml' 
            } 
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}
