pipeline{

    agent {
        node {
           label "dev"
        }
        
    }

    stages{

        stage('Build image'){
            steps{
                sh 'docker build -t flask_app_dev:latest .'
                //sh 'docker container exec bash python train.py'''
                //echo "get code from github"
            }
        }

        stage('train model'){
            steps{
                echo "train model & save it"
            }
        }

        stage('push docker image'){
            steps{
                echo "push docker image to dockerhub"
            }
        }

        stage('deploy'){
            steps{
                sh "docker run -d -p 5000:5000 --name flask-app flask_app_dev:latest"
                echo "deploy code"
            }
        }

    }


    
}