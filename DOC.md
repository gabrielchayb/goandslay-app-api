github // workflows
- checks.yml : Login to Docker Hub, commands to test and lint the app, github actions

docker-compose.yml : commands, environment, ports, etc 
Dockerfile : operational system requirements 
requirements.dev.txt : libs to dev use 
requirements.txt : libs to app use 

App

// app

- settings.py 
- tests.py: arquivo do testes  

// core 
- // management - wait_for_db:
- // migrations: - toda vez que migramos um banco de dados Quando executamos o comando makemigrations, o Django cria o banco de dados e as migrations, mas não as executa, isto é: não realmente aplica as alterações no banco de dados.
Para que o Django as aplique, são necessárias três coisas, basicamente:
1. Que a configuração da interface com o banco de dados esteja descrita no arquivo de configurações settings.py.
2. Que os modelos e migrations estejam definidos para esse projeto.
3. Execução do comando migrate.

- models.py Cada classe dentro de models.py é uma representação de uma tabela no banco de dados, e os atributos dessas classes são mapeados para colunas da tabela.

// recipe 

- serialyzers.py: o propósito dele seria converter os dados dos modelos relacionados a receitas em formatos adequados para envio e recebimento via API. 
	1.	Conversão de Dados:
O serializer transforma dados dos modelos em JSON ou outros formatos para serem consumidos por APIs, além de transformar dados recebidos em objetos Python utilizáveis.
	2.	Validação de Dados:
Ele também permite definir validações personalizadas para garantir que os dados recebidos estejam no formato correto antes de serem salvos no banco de dados.
	3.	Estrutura Básica de um Serializer:
Um serializer geralmente é uma classe que herda de serializers.ModelSerializer ou serializers.Serializer, e define quais campos de um modelo ou dados personalizados serão serializados.

- views.py o arquivo views.py é responsável por lidar com as requisições HTTP e retornar as respostas adequadas. Ele define a lógica que acontece quando um cliente (geralmente um navegador ou uma API) faz uma requisição a uma determinada URL da aplicação.ele contém as funções ou classes que tratam as requisições relacionadas às receitas.

// user 

- mesma logica do recipe

// manage.py é o arquivo que executa toda nossa aplicação, através dos comandos que definimos com o docker-compose

// .dockerignore ignora o venv e outras coisas do tipo.