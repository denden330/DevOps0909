properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/denden330/DevOps0909.git"
    }
    stage("show files"){
        bat "dir"
    }
}
