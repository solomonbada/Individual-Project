pipeline {
        agent any
        stages{
                        stage('---Build_Image---'){
                                steps{
                                        sh "sudo docker build -t webapp ."
                                }
                        }
                        stage('--clean--'){
                                steps{
                                       sh label: '', script: 
                                           '''
                                           if [ "$(sudo docker ps -aq -f name=webapp)" ]; then
                                                sudo docker rm -f webapp
                                           fi
                                           '''
                               }
                        }
                                              
                        stage('--run--'){
                                steps{
                                                                
                                        sh "sudo docker run -d -p 5000:5000 --name flaskapp webapp"
                                 
                                }
                        }
        }
}
