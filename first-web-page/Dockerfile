#init a base image Alpine linux distro
FROM  python:3.6.1-alpine
 
#define the present working directory
WORKDIR /first-web-page


#copy the contents into the working dir
ADD  . /first-web-page

#run pip to install the dependencies of the flask app
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt



# define the command to start the container

CMD python web.py


