#**Bem vindo!** 

Este repositório contém um sistema IPS que foi implementado como trabalho da disciplina de Programação Orientada a Objetos 2. 

###**Pré-requisitos:**

* Python >= 2.7
* VirtualEnv
* PIP
* PostgreSQL >= 9.4
* Git >= 2.6 (Opcional)

### **Instruções:**

Baixe o projeto clicando em **"Download Zip"** ou, caso possua o git instalado, utilize o comando:

`git clone https://github.com/asleao/ips-project-backend.git`

### Execução:

Entre, pelo terminal, na pasta do projeto extraída. Em seguida execute o comando:

`virtualenv virtual`

Este comando criará uma pasta "virtual" no seu projeto com o ambiente virtual do Python. O nome "virtual" pode ser substituído por qualquer um de sua preferência. Em seguida, para ativa-lo digite o comando:

Linux: `source virtual/bin/activate`
Windows: `virtual\Scripts\activate`

Crie em seu PostgreSQL, um banco com o nome "ips". Vá até a pasta "ips" e abra o arquivo "settings.py" em um editor de texto de sua preferência. Na opção "DATABASES" altere o "password" para o que você utiliza.

Se estiver usando linux, para a utilização do banco postgresql, é necessário as dependências libpq-dev e python-dev . Para isso, execute o seguinte comando no terminal:

`sudo apt-get install libpq-dev python-dev`

Se estiver no Windows, o comando acima não é necessário.

Com o ambiente virtual ativado e banco de dados configurado, volte para a pasta principal do projeto, onde o arquivo "requirements.txt" se econtra, e instale as dependências do projeto com o comando:

`pip install -r requirements.txt`

Para criar as tabelas do projeto no banco, para isso entre na pasta "ips" e digite o comando:

`python manage.py migrate`

Para criar um usuário administrador digite o comando:

`python manage.py createsuperuser`

Por fim, para executar o projeto basta executar o comando:

`python manage.py runserver`

Para logar no sistema, digite o seguinte endereço no seu navegador:

`localhost:8000/admin`
