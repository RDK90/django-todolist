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