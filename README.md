# To Do List App

## Introduction
This project is to build upon the Django To Do List app built by [Brad Traversy](https://github.com/bradtraversy/django-todolist). Thanks Brad for the tutorials!

## Prerequisites
Docker - version 19+ [Installation guide](https://docs.docker.com/get-docker/)

Docker-compose - version 3+ [Installation guide](https://docs.docker.com/compose/install/)

## Installation
Clone the repository
```bash
git clone git@github.com:RDK90/django-todolist.git
```
Build the containers using docker-compose
```bash
docker-compose up --build -d
```
Run the containers
```bash
docker-compose up
```
Browse to http://0.0.0.0:8000/todos

## Database Migrations
### Apply Latest Changes
In order to apply the models API changes to the PostgreSQL DB some Django methods need to be implemented. To do this, access the Django container by:
```bash
docker exec -it to_do_web bash
```
Next, migrate the changes
```bash
python manage.py migrate
```
### Apply Developer Changes
If you are editing the models API, then a new migrations file will need to be generated in order to apply these changes to the DB. In this case, access the container as above and run the following command to create the migrations file. 
```bash
python manage.py makemigrations
```
Then apply the migration.
```bash
python manage.py migrate
```

## Run the Tests
Tests for this projects are run using Pytest as included in the requirements.txt. Pytest-Django is also required to pass in the project settings file so pytest knows how to instantiate the application. To run the tests access the container as above and run:
```bash
pytest --ds=todolist.settings
```