# Instawork-backend
Author: Zhaoyi Zhuang

## Overview
This project implements a RESTful HTTP API to support a team-member management application. The application supports common CRUD operations of the team, uses AWS MySQL RDS as the database, and is implemented in Python and Django

## How to setup and install
Tools needed for this project:
* Django
* mysqlclient
* Django REST Framework

## How to run and test the project

To run the project locally
```
python3 manage.py runserver
```

To test the project, open a new terminal window

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
