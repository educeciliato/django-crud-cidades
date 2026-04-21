# Projeto Django CRUD - Cidades

## Funcionalidades Implementadas

Para a classe **Cidade**, foram implementadas as seguintes views:
- **Inserir**: Cadastrar novas cidades (Nome e UF).
- **Alterar**: Editar de dados de cidades já cadastradas.
- **Detalhar**: Visualização detalhada de uma cidade específica.
- **Excluir**: Excluir registros do banco de dados.
- **Listar**: Listar todas as cidades cadastradas.

## Tecnologias Utilizadas

- **Python 3.11**
- **Django 5.x**
- **Django Crispy Forms** (com Bootstrap 5)
- **Bootstrap 5** (para o front-end)
- **SQLite** (banco de dados padrão)

## Como Executar o Projeto
1. Instale as dependências:
   ```bash
   pip install django django-crispy-forms crispy-bootstrap5
   ```
2. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
3. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
4. Acesse `http://127.0.0.1:8000` no seu navegador.
