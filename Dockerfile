# FROM 
# RUN command to exe while building the image
# CMD command to exe while building the contaier we can override it
# ENTRYPOINT command to exe while building the contaier


# CMD  python3 main.py

# docker run -it -exec image bash


# RUN adduser hodi
# USER hodi

# COPY . .

# WORKDIR /app

# '''
#     mkdir app
#     cd app
# '''




# FROM ubuntu
# COPY file1.txt .
# WORKDIR /app
# ADD file2.txt /app/


# pwd? ->              /app
# path file2? ->       /app/file2.txt
# path file1?->       /file1.txt



# npm i 
# pip3 install -r req.txt
# mvn spring

# run chmod 777 hodi.sh
# cmd ./hodi.sh



docker build -t hodi:v1 .

docker rmi -f $(docker images -qa)

docker run -p host port : container port

docker ps -a 
docker kill stop 
docker run -v 


contaier - virtual machine 
iso - image

docker prune 

docker run :latest

