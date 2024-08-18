pipeline{

    agent {
        node {
           label "dev"
        }
        
    }

    stages{

        stage('clone git code'){
            steps{
                echo "get code from github"
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
                echo "deploy code"
            }
        }

    }


    
}