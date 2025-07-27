pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                sh '''
                echo "开始拉取代码..."
                '''
                git branch: 'main', url: 'https://github.com/18naive/demo.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // 使用 BUILD_NUMBER 作为镜像标签
                    def imageName = "my-app:${env.BUILD_NUMBER}"
                    
                    // 构建镜像
                    docker.build(imageName)
                    
                    // 保存镜像信息
                    currentBuild.description = "Image: ${imageName}"
                }
            }
        }
    }
    
    post {
        always {
            // 清理工作空间
            cleanWs()
        }
    }
}