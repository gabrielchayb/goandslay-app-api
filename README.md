A teaching plataform that allows clients to log in using token-based authentication to manage their lessons with titles, contents and much more. it is focused on developing, documenting, and maintaining scalable and secure RESTful APIs, built using Django and PostgreSQL. The project uses Docker to facilitate containerization and deployment, and Django REST Framework (DRF) to create a robust RESTful API for recipe management.

Features:

	•	CRUD Operations: Create, read, update, and delete recipes.
	•	Filtering and Search: Search recipes by tags, ingredients, number of ingredients, etc.
	•	Recipe Categorization: Add images to your recipes, tags for filtering, unlimited ingredients, time, cost, description, etc.
	•	Authentication: Secure user authentication using Django’s integrated token system.
	•	PostgreSQL Database: Efficient storage and management of relational data.
	•	Docker: Containerized environment for easy setup and deployment.

Tech Stack:

	•	Django: Backend framework for Python.
	•	Django REST Framework: REST API framework for Django.
	•	PostgreSQL: Relational database management system.
	•	Docker: Containerization for development and production.
	•	GitHub Actions: Maintenance of pipelines, CI/CD for production.
	•	SwaggerUI: Complete documentation of the RESTful APIs, including endpoints, authenticated testing, requests, schemas, etc. Available at localhost/api/docs.

Instalação:

	1.	Clone este repositório.
	2.	Configure a sua imagem do Docker (ligue ele localmente).
	3.	Suba seu servidor com: docker-compose up (ele ja vai instalar tudo pois foi configurado no Dockerfile, fique tranquilo)
 	4.	Consulte e teste a documentação das APIs em: http://127.0.0.1:8000/api/docs/
  	5.      Não se esqueça de autenticar seu user: em apis user, /api/user/token/ , faça login, copie e cole o token gerado, e em cima da page, clique em "Authorize", clique em tokenAuth, e digite no campo, desse jeito: Token: xxxxxxxxxxxxxxxxxxxxx 