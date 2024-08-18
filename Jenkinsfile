pipeline{

    agent {
        node {
           label "dev"
        }
        
    }

    environment {
        DOCKER_IMAGE = 'flask-app-dev'
        CONTAINER_NAME = "flask-app"
        //DOCKERHUB_CREDENTIALS=credentials('dockerhub-credentials')
    }

    stages{

        stage('Build image'){
            steps{
                echo "Building image..."
                sh 'docker build -t $DOCKER_IMAGE:latest .'
                //sh 'docker container exec bash python train.py'''
                //echo "get code from github"
            }
        }

        stage('train model'){
            steps{
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
                sh 'docker run --name $CONTAINER_NAME $DOCKER_IMAGE /bin/bash -c "python train.py"'
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
                echo "Deploying..!"
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
                sh "docker run -d -p 5000:5000 --name $CONTAINER_NAME $DOCKER_IMAGE:latest"
                echo "deploy code"
            }
        }

    }


    
}