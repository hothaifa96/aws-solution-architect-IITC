import os

image_name = os.environ.get('IMAGE_NAME')
des_port= 5000
ta_port=5010
containername='hodizzzone'


os.system('docker rm -f $(docker ps -qa)')
os.system(f'docker run -p {ta_port}:{des_port} --name {containername} {image_name}')