# Sistema de Gerenciamento de Banco de Dados com PostgreSQL

Este projeto cria um sistema de gerenciamento de banco de dados para gerenciar um banco de dados de clientes utilizando PostgreSQL e Python.

## Estrutura do Projeto

gerenciamento-banco-dados/
│
├── src/
│   └── gerenciamento_banco.py
│
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── init_db.sql


## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciamento-banco-dados.git
   cd gerenciamento-banco-dados

2.  Construa a imagem Docker:
    docker-compose up --build

3.  Execute o script de gerenciamento:
    docker-compose run app python src/gerenciamento_banco.py

