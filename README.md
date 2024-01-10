# TACO API USERS SERVICE

### Descrição

Esse projeto é um Microserviço criado para gerenciar o cadastro de novos usuários que desejam usar a TACO-API (wip). 
Ela também providência uma API-KEY para o usuário cadastrado realizar a autenticação toda a vez que for realizar chamadas na TACO-API (wip).

## Tecnologias

* FastAPI
* MongoDB (beanie)
* RabbitMQ (pika)
* Python 3.12

## Observações

Antes de iniciar, você deve criar um arquivo .env na raiz do projeto para estabelecer os valores de banco de dados e messageria.

| Variável | Descrição |
| -------- | ------- |
| DB_HOST  | Host de conexão do MongoDB |
| DB_NAME | Nome da base de dados a ser utilizada |
| DB_USERNAME | Nome do usuário do banco de dados |
| DB_PASSWORD | Senha de acesso ao banco de dados |
| AMQP_HOST | Host de conexão com o RabbitMQ |
| AMQP_VHOST | Nome do vhost da conexão do RabbitMQ |
| AMQP_USERNAME | Nome do usuário de conexão com o RabbitMQ |
| AMQP_PASSWORD | Senha de conexão do RabbitMQ |

OBS: Foi usado o RabbitMQ Cloud e MongoDB Cloud para realizar o desenvolvimento desse projeto

## Endpoints

v.0.0.1  
* GET - /api/users/{user_id} - Retorna um usuário dado seu ID
* POST - /api/users - Cadastra um novo usuário


