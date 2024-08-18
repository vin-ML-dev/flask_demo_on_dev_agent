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
                //sh 'docker container exec $CONTAINER_NAME python train.py'
                sh 'docker run --name $CONTAINER_NAME $DOCKER_IMAGE /bin/bash -c "python train.py"'
                sh "docker cp $CONTAINER_NAME:/app/iris_model.pkl ."
               
                echo "train model & save it"
            }
        }

        stage('push docker image'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerhubcreds', passwordVariable: 'dockerhubpass', usernameVariable: 'dockerhubuser')]) 
                {
                    sh "docker image tag $DOCKER_IMAGE:latest ${env.dockerhubuser}/$DOCKER_IMAGE:latest"
                    sh "docker login -u ${env.dockerhubuser} -p ${env.dockerhubpass}"
                    sh "docker push ${env.dockerhubuser}/$DOCKER_IMAGE:latest"
                }
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