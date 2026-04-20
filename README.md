# Projeto Django CRUD - Cidades

Este projeto foi desenvolvido como parte de uma atividade prática para implementar as operações básicas de um sistema (CRUD) utilizando o framework Django.

## Funcionalidades Implementadas

Para a classe **Cidade**, foram implementadas as seguintes views:
- **Inserir**: Cadastro de novas cidades (Nome e UF).
- **Alterar**: Edição de dados de cidades existentes.
- **Detalhar**: Visualização detalhada de uma cidade específica.
- **Excluir**: Remoção de registros do banco de dados.
- **Listar**: Listagem paginada de todas as cidades cadastradas.

## Tecnologias Utilizadas

- **Python 3.11**
- **Django 5.x**
- **Django Crispy Forms** (com Bootstrap 5)
- **Bootstrap 5** (para o front-end)
- **SQLite** (banco de dados padrão)

## Como Executar o Projeto

1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install django django-crispy-forms crispy-bootstrap5
   ```
3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
5. Acesse `http://127.0.0.1:8000` no seu navegador.

---
**Desenvolvido por Manus AI**
