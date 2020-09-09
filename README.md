## Instalação via Docker

* Executando o banco de dados juntamente com a api sem dedicar o terminal para o docker:
	```
	$ docker-compose up -d
	```
* **Nota:** Remova o -d para continuar no terminal do docker. Caso ocorra algum problema em relação à conexão TCP/IP na porta 5432, reinicie o container sem deletá-lo.

* Encerrando o container sem estar no terminal do docker:
	```
	$ docker-compose stop
	```
* **Nota:** Caso esteja no terminal, utilize o comando ctrl+c.

#### Testes
* Com o docker-compose rodando, utilize o seguinte comando em um novo terminal:
  ```
  $ docker exec -it <id do container> sh
  ```
* **Nota:** Para verificar o id do container, utilize o comando "docker ps" e procure o ID correspondente a imagem "api-transacao_api"

* Acessando o container, tenha certeza de que está na pasta backend/ e digite:
  ```
	$ coverage run manage.py test
	```
* É possível verificar a cobertura dos testes executando:
	```
	$ coverage report
	```

#### Endpoints

* endpoint base:
	```
	http://127.0.0.1:8000
	```

* Sintaxe de requisição para registrar uma transação:

		response = client.post(
			"/api/v1/transacao/",
			data={
				"estabelecimento": "String",
				"cliente": "String",
				"valor": Float,
				"descricao": "String"
			}
		)

* Sintaxe de resposta para registrar uma transação:
	
		{
			"envio": True
		}

* Sintaxe de requisição para buscar todas transações:

		response = client.get(
			"/api/v1/transacao/"
		)

* Sintaxe de resposta para buscar todas transações:
	
		[
			{
				"id": Int,
				"estabelecimento": "String",
				"cliente": "String",
				"valor": Float,
				"descricao": "String"
			}
		]


#### Tabela de status

| Código | Status |
|:-------:|:---------:|
| 200   | OK |
| 201   | CREATED |
| 400   | BAD_REQUEST |
