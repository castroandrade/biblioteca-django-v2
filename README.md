# Exercício Prático - Unidade 6 - Trilha Backend

**Nome:** José Henrique Castro Andrade

## Instruções

### 1. Clone do Repositório

```bash
git clone https://github.com/castroandrade/biblioteca-django-v2.git
cd biblioteca-django-v2
```

### 2. Criação do Ambiente Virtual e Instalação de Dependências

```bash
python -m venv venv
```
Ative o ambiente virtual:

- No Linux/macOS:
  ```bash
  source venv/bin/activate
  ```
- No Windows:
  ```bash
  .\venv\Scripts\activate
  ```

Instale as depedências:

```bash
pip install -r requirements.txt
```

### 3. Migrações e População do Banco de Dados

Execute os seguintes para criar e executar as migrações e popular o banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py populate_db
```

### 4. Iniciar Servidor Django

Para iniciar o servidor digite o comando:

```bash
python manage.py runserver
```
