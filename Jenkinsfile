pipeline {
    agent any

    options {
        ansiColor('xterm')
    }
    parameters{
        choice(name: 'Stage', choices: ['dev', 'test', 'staging', 'production'], description: 'Deployment stage')
    }
    stages {
        stage('Serverles Deploy') {
            environment {
                AWS_DEFAULT_REGION = "us-east-1"
                SECRETS_PATH = "dmiint-dmicreds/sms-serverless-dev.env"
            }
            steps {
                // sh 'virtualenv --python=python3.6 venv'
                nodejs(nodeJSInstallationName: 'nodejs-8.12.0', configId: 'ce521769-a223-47c7-bbe9-d54cb3f782b8') {
                    dir("${env.WORKSPACE}") {
                        sh 'rm -rf node_modules'
                        sh 'npm install'
                        withAWS(credentials: 'ngs-aws-dev-terraform', region: 'us-east-1') {
                            
                        sh """#!/bin/bash -xe
                        echo "----------- start ------------"
                        ls
                        aws s3 cp s3://$SECRETS_PATH  .env
                        eval \$(cat .env | sed 's/^/export /')                            
                        
                        echo "Deploying using Serverless Framework"
                        npx serverless deploy --stage $Stage
                        """
                           
                        }
                    }
                }
            }
        }
        
  
    }
    post {
        failure {
            slackSend channel: '#earthpulse-build',
                color: 'danger',
                message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Failure (<${env.BUILD_URL}|Open>)"
        }
        success {
            slackSend channel: '#earthpulse-build',
                color: 'good',
                message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} New build available: (<${env.BUILD_URL}|Build Info>)"
        }
    }
}
