pipeline {
    agent { label "suraj" }
    
    stages {
        stage("Clone") {
            steps {
                echo "Cloning the code from GitHub"
                git url: "https://github.com/suraj-v86/ci-cd_project.git", branch: "main"
            }
        }
        stage("Build") {
            steps {
                echo "Building docker image"
                sh "docker build -t python-app:latest ."
            }
        }
        stage("Push") {
            steps {
                echo "Push the docker image to Dockerhub"
                withCredentials([usernamePassword(
                    credentialsId: "dockerhubCred",
                    usernameVariable: "dockerhubUser",
                    passwordVariable: "dockerhubPass"
                )]) {
                    echo "Logging into Dockerhub"
                    sh "docker login -u ${dockerhubUser} -p ${dockerhubPass}"
                    
                    echo "Tagging and pushing image"
                    sh "docker image tag python-app:latest ${dockerhubUser}/python-app:latest"
                    sh "docker push ${dockerhubUser}/python-app:latest"
                }
            }
        }
        stage("Deploy") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "dockerhubCred",
                    usernameVariable: "dockerhubUser",
                    passwordVariable: "dockerhubPass"
                )]) {
                    echo "Deploying the container"
                    sh "docker rm -f python-app || true"
                    sh "docker pull ${dockerhubUser}/python-app:latest"
                    sh "docker run -d -p 5000:5000 --name python-app ${dockerhubUser}/python-app:latest"
                }
            }
        }
    }
}
