# Thesis - Data-Quality

## Create virtual environment with docker

### build image from Dockerfile
 docker build -t thesis .

### from image to container
docker run --rm -d -p 9000:8888 -p 4041:4040 -e DOCKER_STACKS_JUPYTER_CMD=nbclassic --user root -e GRANT_SUDO=yes  -v ${PWD}:/home/jovyan/ --name container_thesis thesis  

docker run --rm -d -p 9000:8888 -p 4040:4040 -e DOCKER_STACKS_JUPYTER_CMD=nbclassic --user root -e GRANT_SUDO=yes  -v %cd%:/home/jovyan/ --name container_thesis thesis


### localhost
open in broswer
http://localhost:9000/
password is 'DQ2022'


Data Ingestion Workflow

![image](https://user-images.githubusercontent.com/58252186/222507141-706b9436-6407-4ebb-8e78-b1fc70e53a51.png)
