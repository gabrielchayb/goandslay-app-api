This page is a resume to all the app structure

GitHub // Workflows

	•	checks.yml: Logs in to Docker Hub, runs commands to test and lint the app using GitHub Actions.
	•	docker-compose.yml: Contains commands, environment variables, ports, etc.
	•	Dockerfile: Specifies the operational system requirements.
	•	requirements.dev.txt: Lists libraries used for development.
	•	requirements.txt: Lists libraries used by the application in production.

App Structure

// app

	•	settings.py: Contains all the application configurations.
	•	tests.py: File for unit and integration tests.

// core

	•	management - wait_for_db: Since there is a timing discrepancy between Docker Compose and PostgreSQL, we add a “test” that waits for PostgreSQL to be ready before Docker Compose builds the application.
	•	migrations: Every time we migrate a database, running the makemigrations command creates database migrations in Django, but it doesn’t apply the changes. To apply the changes, three steps are needed:
	1.	Ensure the database interface is configured in settings.py.
	2.	Make sure models and migrations are defined for the project.
	3.	Run the migrate command to apply the migrations.
	•	models.py: Each class in models.py represents a database table, and the class attributes map to the columns in that table.
	•	templates - pasta where our html files are;
	•	tests: some tests that I created to validated my functions
	
// licao (lesson)

	•	serializers.py: The purpose of this file is to convert the lesson-related model data into formats suitable for API requests and responses.
	1.	Data Conversion: The serializer transforms model data into JSON or other formats to be consumed by APIs, and it converts received data into usable Python objects.
	2.	Data Validation: It allows custom validations to ensure the received data is in the correct format before saving it to the database.
	3.	Basic Structure of a Serializer: A serializer is usually a class that inherits from serializers.ModelSerializer or serializers.Serializer, defining which fields of a model or custom data will be serialized.
	•	views.py: Handles HTTP requests and returns the appropriate responses. It defines the logic that happens when a client (usually a browser or an API) makes a request to a specific URL in the application. It contains the functions or classes that handle the lesson-related requests.

// user

	•	Follows the same logic as the lesson module.

// manage.py

	•	This file runs the entire application, executed through the commands defined with docker-compose.

// .dockerignore

	•	Ignores the venv and other unnecessary files or directories.

Admin Access

	•	Admin Login URL: http://127.0.0.1:8000/admin/login/?next=/admin/
	•	Login: admin@gmail.com
	•	Password: sssss
