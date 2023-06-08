import os


# image name
image_name=os.environ.get('IMAGE_NAME')
#

#
os.system(f'docker build -t {image_name} {os.getcwd()}')

