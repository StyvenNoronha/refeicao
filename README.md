README - API de Refeições com Flask

Descrição:
Esta é uma API simples desenvolvida com Flask que permite cadastrar, visualizar, atualizar e deletar refeições. As refeições incluem informações como nome, descrição, data/hora e se estão ou não dentro da dieta.

Requisitos:
- Python 3.x  
- Flask  
- SQLAlchemy  

Instalação:
1. Clone este repositório.
2. Instale os pacotes necessários:
   pip install Flask SQLAlchemy
3. Execute o projeto:
   python app.py

Endpoints Disponíveis:

- GET /
  Retorna uma mensagem padrão: {"message": "refeição"}

- POST /create
  Cria uma nova refeição.  
  Exemplo de JSON:
  {
    "name": "Almoço",
    "description": "Arroz e feijão",
    "date_time": "2025-05-12T12:00:00",
    "within_the_diet": true
  }

- GET /refeicoes
  Lista todas as refeições cadastradas.

- GET /refeicao/<id>
  Retorna os dados de uma refeição específica pelo ID.

- PUT /refeicao/<id>
  Atualiza os dados de uma refeição existente.  
  Exemplo de JSON:
  {
    "name": "Jantar",
    "description": "Salada e frango",
    "within_the_diet": false
  }

- DELETE /refeicao/<id>
  Deleta uma refeição com base no ID.

Observações:
- O banco de dados utilizado é SQLite e será criado automaticamente como database.db.
- A modelagem da classe Refeicao está localizada em models/refeicao.py.
- O código está em desenvolvimento e pode ser estendido com autenticação, filtros, etc.
