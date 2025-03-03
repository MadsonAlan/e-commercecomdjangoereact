# ️ E-commerce com Django e React

Este projeto é uma loja online completa, desenvolvida com Python Django no backend e React no frontend.

##  Tecnologias Utilizadas

* **Backend:**
    * Python <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
    * Django <img align="center" alt="Django" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-plain.svg">
    * Django Rest Framework
    * PostgreSQL (ou outro banco de dados de sua preferência) <img align="center" alt="PostgreSQL" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg">
* **Frontend:**
    * React <img align="center" alt="React" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg">
    * JavaScript <img align="center" alt="JavaScript" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg">
    * HTML5 <img align="center" alt="HTML5" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg">
    * CSS3 <img align="center" alt="CSS3" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg">

## ⚙️ Como Rodar o Projeto

### 1. Backend (Django)

1.  Clone o repositório:

    ```bash
    git clone [https://github.com/robsonmmfata/e-commercecomdjangoereact.git](https://github.com/robsonmmfata/e-commercecomdjangoereact.git)
    cd e-commercecomdjangoereact/backend
    ```

2.  Crie um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate # No Linux/macOS
    venv\Scripts\activate # No Windows
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4.  Configure o banco de dados:
    * configure as variaveis de ambiente de acordo com seu banco de dados.
    * Aplique as migrações:

        ```bash
        python manage.py migrate
        ```

5.  Crie um superusuário:

    ```bash
    python manage.py createsuperuser
    ```

6.  Execute o servidor:

    ```bash
    python manage.py runserver
    ```

### 2. Frontend (React)

1.  Navegue até o diretório do frontend:

    ```bash
    cd ../frontend
    ```

2.  Instale as dependências:

    ```bash
    npm install
    ```

3.  Execute o frontend:

    ```bash
    npm start
    ```

##  Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

##  Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

Feito com ❤️ por Robsonmmfata.
