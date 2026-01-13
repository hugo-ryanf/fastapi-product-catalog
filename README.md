# 🛒 FastAPI Product Catalog API

> API RESTful robusta para gerenciamento de produtos de e-commerce com autenticação JWT segura.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📋 Sobre o Projeto

Este projeto é o backend de um sistema de e-commerce. O objetivo foi criar uma arquitetura escalável e segura onde usuários autenticados podem gerenciar um inventário de produtos. O sistema implementa validação rigorosa de dados e segurança via tokens.

<img width="1808" height="939" alt="Captura de tela 2026-01-13 161957" src="https://github.com/user-attachments/assets/a36f773f-7238-4e10-bad3-9bdb2bca71bd" />

## 🚀 Tecnologia![Uploading Captura de tela 2026-01-13 161957.png…]()
s Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno e de alta performance.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM para gerenciamento e persistência de dados.
- **[Pydantic](https://docs.pydantic.dev/):** Validação de dados e serialização.
- **[Passlib](https://passlib.readthedocs.io/):** Hashing de senhas (segurança).
- **[Python-Jose](https://python-jose.readthedocs.io/):** Gerenciamento de tokens JWT (JSON Web Tokens).
- **SQLite:** Banco de dados relacional (SQL).

## ✨ Funcionalidades Principais

- ✅ **Autenticação Segura:** Sistema de login com geração e validação de Tokens JWT.
- ✅ **CRUD Completo:** Create, Read, Update e Delete de produtos.
- ✅ **Proteção de Rotas:** Apenas usuários logados podem adicionar ou remover itens.
- ✅ **Documentação Automática:** Swagger UI e ReDoc integrados.

## ⚙️ Como Rodar o Projeto Localmente

Siga os passos abaixo para testar a API no seu computador:

### 1. Clone o repositório
```
git clone git clone https://github.com/hugo-ryanf/fastapi-product-catalog.git
cd fastapi-product-catalog
``` 
3. Instale as Dependências
```
pip install -r requirements.txt
```

4. Execute o Servidor
```
python -m uvicorn app.main:app --reload
```
A API estará rodando em: http://127.0.0.1:8000

📚 Documentação da API
Acesse a documentação interativa para testar os endpoints:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

### Principais Endpoints

| Método | Endpoint | Descrição | Autenticação? |
| :--- | :--- | :--- | :---: |
| `POST` | `/auth/token` | Faz login e recebe o Token de acesso | ❌ |
| `GET` | `/produtos` | Lista todos os produtos do catálogo | ❌ |
| `POST` | `/produtos` | Cria um novo produto | ✅ |
| `PUT` | `/produtos/{id}` | Atualiza os dados de um produto | ✅ |
| `DELETE` | `/produtos/{id}` | Remove um produto do catálogo | ✅ |



👨‍💻 Autor: 
Desenvolvido por Hugo Ryan.

