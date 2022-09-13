#Deriving the latest base image
FROM python:latest


#Install required module
RUN pip install requests


# Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /home

#to COPY the remote file at working directory in container
COPY macaddress.py ./
# Now the structure looks like this '/home/macaddress.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
 
CMD [ "python", "./macaddress.py"]
