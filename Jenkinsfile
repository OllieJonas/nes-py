pipeline {
    agent any
    environment {
        PROJECT_NAME = 'nes-py'
        DEPLOY_DIR_NAME = "${env.PROJECT_NAME}"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building ${env.PROJECT_NAME} on ${env.JENKINS_URL}..."
                sh "mkdir ${env.DEPLOY_DIR_NAME}"
                sh "zsh --version"
                sh "bash --version"
                sh "shopt -s extglob"
                sh "mv !(${env.DEPLOY_DIR_NAME}) ${env.DEPLOY_DIR_NAME}"
                sh "tar -czvf ${env.PROJECT_NAME}.tar.gz ${env.DEPLOY_DIR_NAME}"
            }
        }

        stage('Deploy') {
            environment {
                DEPLOY_SERVER_URL = "olliejonas.com"
                DEPLOY_SERVER_USER = "root"

                TARGET_DIR = "/home/ollie/Projects/Dissertation/${PROJECT_NAME}"
                PYTHON_PACKAGES_DIR = "/home/ollie/Projects/python-packages"
            }
            steps {
                script {
                    env.DEPLOY_SERVER = "${env.DEPLOY_SERVER_USER}@${env.DEPLOY_SERVER_URL}"
                }
                echo "Deploying ${env.PROJECT_NAME} to ${env.DEPLOY_SERVER_URL}..."

                sshagent(credentials: ['projects']) {
                    sh """
                        [ -d ~/.ssh ] || mkdir ~/.ssh && chmod 0700 ~/.ssh
                        ssh-keyscan -t rsa,dsa ${DEPLOY_SERVER_URL} >> ~/.ssh/known_hosts
                        scp ${env.PROJECT_NAME}.tar.gz ${env.DEPLOY_SERVER}:${env.TARGET_DIR}

                        ssh -t -t ${env.DEPLOY_SERVER} << EOF
                        cd ${env.TARGET_DIR}
                        python3 setup.py sdist
                        mv dist/* ${PYTHON_PACKAGES_DIR}
                        exit
                        EOF
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Performing cleanup..."
            sh "rm -rf ${env.DEPLOY_DIR_NAME}"
            sh "rm -f ${env.PROJECT_NAME}.tar.gz"
        }
    }
}