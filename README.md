# Instawork-backend
Author: Zhaoyi Zhuang

## Overview
This project implements a RESTful HTTP API to support a team-member management application. The application supports common CRUD operations of the team, uses AWS MySQL RDS as the database, and is implemented in Python and Django

## How to setup and install
I assume you have already installed python, if not, check out [this website](https://www.python.org/downloads/)

Tools needed for this project:
* Django
* mysqlclient
* Django REST Framework

### Install Django
running the following command in shell to check if you have a Django installed already
```
python -m django --version
```
or
```
python3 -m django --version
```
If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”. 
To install Django, using
```
python -m pip install Django
```
See [How to install Django](https://docs.djangoproject.com/en/4.0/topics/install/) for advice


### Install mysqlclient
Then you will need to install mysqlclient
```
brew install mysql
pip3 install mysqlclient
python3 -m pip install PyMySQL
```
for more information, please check out [mysqlclient website](https://pypi.org/project/mysqlclient/)


### Install Django REST Framework
Then you will need to install Django REST Framework using
```
pip install djangorestframework
```
or
```
pip3 install django_rest_framework    
```
If you failed in above two, you may try
```
python3 -m pip install djangorestframework      
```
For more information, please check out [it's website](https://www.django-rest-framework.org/)


## How to run and test the project

To run the project locally, on the root of the project
```
python3 manage.py runserver
```

If you already have a Postman, you can [click this link](https://www.getpostman.com/collections/610751c2c5d1e0046755) to test the project more easily


Otherwise, open a new terminal window

Note: http endpoints for put and delete are users/:uid, so you need to change the uid in link.

POST
```
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/users/ -d '{"first_name":"xxx","last_name":"zzz","phone_number":"123123123","email":"xx@xx.com","role":"regular"}'
```

GET
```
curl -X GET http://127.0.0.1:8000/users/
```

PUT
```
curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/users/12 -d '{"first_name":"Super","last_name":"Rose","role":"admin","superpower":"unkown"}'
```

DELETE
```
curl -X DELETE http://127.0.0.1:8000/users/6
```
