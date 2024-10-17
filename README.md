English Teaching Platform

An English teaching platform that enables clients to log in using token-based authentication to manage their lessons, including titles, content, and more. The project focuses on developing, documenting, and maintaining scalable and secure RESTful APIs, built with Django and PostgreSQL. It utilizes Docker for containerization and deployment, and Django REST Framework (DRF) to create a robust RESTful API for recipe management.

Table of Contents

	•	Overview
	•	API Documentation
	•	Features
	•	Tech Stack
	•	Installation
	•	Usage
	•	Docker Commands

Overview

This platform provides a comprehensive environment for managing English lessons, facilitating CRUD operations for users and lessons while ensuring secure authentication through Django’s integrated token system.

API Documentation

All REST APIs are documented at /api/docs, with SwaggerUI providing:

	•	Listing of all endpoints
	•	Simulation of real API requests from the web, with curl
	•	Manual token authentication with Django Token Auth
	•	Full documentation of all APIs in the system, including responses, HTTP methods, and token authentication

Features

	•	CRUD Operations for Users: Create, read, update, and delete user accounts.
	•	CRUD Operations for Lessons: Create, read, update, and delete lessons, identified by ID.
	•	Lesson Management: Explore every user lesson with details such as title, content, reading time in minutes, price, and link.
	•	Secure Authentication: User authentication using Django’s integrated token system.
	•	PostgreSQL Database: Efficient storage and management of relational data.
	•	Docker: Containerized environment for easy setup and deployment.

Tech Stack

	•	Django: Backend framework for Python.
	•	Django REST Framework: REST API framework for Django.
	•	PostgreSQL: Relational database management system.
	•	Docker: Containerization for development and production.
	•	GitHub Actions: Maintenance of pipelines and CI/CD for production.
	•	SwaggerUI: Complete documentation of the RESTful APIs, including endpoints, authenticated testing, requests, schemas, etc., available at http://localhost/api/docs.

Installation

	1.	Clone this repository.
	2.	Install Docker Desktop on your machine from the following link: Docker Desktop. Log in/create an account and follow the tutorial.
	3.	Configure your Docker image (start Docker Desktop locally and click on “Images”). It will automatically search for images on your machine.
	4.	After cloning the repository to your preferred code editor, run the following command:

docker-compose up

(This command will install everything as configured in the Dockerfile. It may take between 180 to 300 seconds. Please be patient!)

	5.	Access and test the API documentation at: API Docs
	6.	Authenticate your user by navigating to /api/user/token/, logging in, copying the generated token, and clicking “Authorize” at the top of the page. Enter the token in the following format: Token xxxxxxxxxxxxxxxxxxxxx.

Usage

To test all APIs in SwaggerUI, follow this sequence:

	1.	User
	•	POST /api/user/create/ (Create your user)
	•	POST /api/user/token/ (Log in with your user and receive your authorization token)
At the top of the page, click “Authorize” and enter:

	tokenAuth 
	Token xxxxxxxxxxxxxxxxxxxxx


	2.	User Details
	•	GET /api/user/me/ (Check if your user has been authenticated successfully; your login information will be returned)
	•	Test PATCH, PUT, DELETE requests freely.
	3.	Lesson
	•	POST /api/licao/licao (Insert a lesson)
	•	Test GET, PUT, PATCH, GET BY ID, DELETE requests freely.

Docker Commands

For Evaluators

Simply run:

	docker-compose up

For Developers

Run the following commands as needed:

	docker-compose run --rm app sh -c "python manage.py runserver"
	docker-compose run --rm app sh -c "python manage.py makemigrations"
	docker-compose run --rm app sh -c "python manage.py createsuperuser"
	docker-compose run --rm app sh -c "python manage.py migrate"
	docker-compose run --rm app sh -c "python manage.py startapp licao"
	docker-compose -f docker-compose-deploy.yml down
	docker-compose -f docker-compose-deploy.yml up  
	docker-compose up
	docker-compose down
