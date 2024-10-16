A english teaching plataform that allows clients to log in using token-based authentication to manage their lessons with titles, contents and much more. It is focused on developing, documenting, and maintaining scalable and secure RESTful APIs, built using Django and PostgreSQL. The project uses Docker to facilitate containerization and deployment, and Django REST Framework (DRF) to create a robust RESTful API for recipe management.

PS: the documentation of all RESTApis is on /api/docs, with SwaggerUI responsible for:
	•	Listing all endpoints 
	•	Simulating real API requisitions from web, with curl.
	•	Full Documentation of all APIs in the system, including responses, HTTP methods and token authentications.

Description of the app:

	•	CRUD Operations: Create, read, update, and delete users.
	•	CRUD Operations: Create, read, update, and delete lessons, identified by id.
	•	Plus Lessons: Explore every user lesson with: title, content, time in minutes for reading the lesson, price and the link.
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
	(INSTALE O DOCKER DESKTOP EM SUA MAQUINA, NESTE LINK: https://www.docker.com/products/docker-desktop/)
	Faça o login / crie uma conta e continue o tutorial: 
	2.	Configure a sua imagem do Docker (ligue o docker desktop localmente e clique em "Images"). Automaticamente ele vai buscar por imagens na sua maquina.
	3.	Depois de clonar o repositorio para seu editor de codigo favorito, digite: docker-compose up (ele ja vai instalar tudo pois foi configurado no Dockerfile, mas como é muita coisa, geralmente demora de 180 a 300 segundos. Seja paciente!)
 	4.	Consulte e teste a documentação das APIs em: http://127.0.0.1:8000/api/docs/
  	5.  Não se esqueça de autenticar seu user: em apis user, /api/user/token/ , faça login, copie e cole o token gerado, e em cima da page, clique em "Authorize", clique em tokenAuth, e digite no campo, desse jeito: Token xxxxxxxxxxxxxxxxxxxxx 

OBS: para testar todas as apis no SwaggerUI, siga essa ordem: 

1. user

POST
​/api​/user​/create​/ (crie seu usuario)

POST
​/api​/user​/token​/ (faça login com seu usuario e receba seu token de autorização)

No inicio da pagina, clique em Authorize 
tokenAuth 
Token xxxxxxxxxxxxxxxxxxxxx

2. user 

GET 

​/api​/user​/me​/ (teste se o seu usuario foi autenticado com sucesso, se sim, suas informações de login irão ser retornadas)

PATCH, PUT, DELETE (fique a vontade para testar essas requisições)

3. licao 

POST 

/api/licao/licao (insira uma licao)

GET, PUT, PATCH, GET BY ID, DELETE (fique a vontade para testar essas requisições)


COMANDOS PARA RODAR DOCKER

PARA AVALIADORES: precisa apenas rodar docker-compose up

PARA MIM: 
docker-compose run --rm app sh -c "python manage.py runserver" 
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py startapp licao"
docker-compose up
docker-compose down 
