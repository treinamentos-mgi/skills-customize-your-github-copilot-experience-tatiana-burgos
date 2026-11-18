# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para cadastrar e gerenciar livros usando FastAPI. Você vai praticar métodos HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Implement CRUD Endpoints

#### Descrição
Complete o código inicial para criar uma API de livros. Os dados podem ficar em memória durante a execução; não é necessário usar um banco de dados.

#### Requisitos
O programa concluído deve:

- Listar livros com `GET /books`
- Buscar um livro pelo identificador com `GET /books/{book_id}` e retornar `404` quando ele não existir
- Criar um livro com `POST /books`, gerando o identificador no servidor e retornando `201`
- Atualizar todos os dados de um livro com `PUT /books/{book_id}`
- Remover um livro com `DELETE /books/{book_id}` e retornar `404` quando ele não existir

### 🛠️ Validate Requests and Check the API

#### Descrição
Use os modelos Pydantic do FastAPI para validar os dados enviados. Inicie o servidor e experimente cada rota pela documentação interativa.

#### Requisitos
O programa concluído deve:

- Exigir título e autor não vazios e aceitar o ano de publicação como número inteiro
- Retornar `404` para operações de busca, atualização ou remoção de um livro inexistente
- Exibir a documentação interativa em `/docs`
- Ser executável com `uvicorn starter-code:app --reload` após instalar as dependências com `python -m pip install fastapi uvicorn`