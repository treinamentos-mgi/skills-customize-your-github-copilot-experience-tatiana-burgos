# 📘 Atividade: API de Biblioteca com SQLite

## 🎯 Objetivo

Amplie uma API REST com FastAPI para persistir os dados de livros em um banco SQLite. Você praticará criação de tabelas e operações CRUD com SQL parametrizado, mantendo os códigos HTTP apropriados.

## 📝 Tarefas

### 🛠️ Criar o banco de dados e a tabela de livros

#### Descrição
Complete `initialize_database()` no código inicial para criar o banco `books.db` e a tabela que armazenará os livros. A inicialização deve poder ser executada mais de uma vez sem apagar os dados existentes.

#### Requisitos
O programa concluído deve:

- Criar uma tabela `books` com `id` inteiro como chave primária autoincremental
- Armazenar título, autor e ano de publicação
- Criar a tabela apenas se ela ainda não existir
- Fechar a conexão com o banco após a inicialização

### 🛠️ Persistir as operações da API

#### Descrição
Substitua as implementações incompletas dos endpoints para que usem SQLite em vez de uma coleção em memória. Os dados devem continuar disponíveis depois que o servidor for encerrado e iniciado novamente.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` e `GET /books/{book_id}` usando dados do banco
- Implementar `POST /books`, gerando o identificador no banco e retornando `201`
- Implementar `PUT /books/{book_id}` e `DELETE /books/{book_id}`, retornando `404` quando o livro não existir
- Usar parâmetros SQL para todos os valores recebidos pela API
- Retornar `204` ao excluir um livro existente e validar cada rota em `/docs`

Instale as dependências com `python -m pip install fastapi uvicorn` e inicie a API com `uvicorn starter-code:app --reload`. O módulo `sqlite3` já faz parte da biblioteca padrão do Python.
