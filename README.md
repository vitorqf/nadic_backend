<h1 align='center'>~/trilha_NADIC/backend</h1>

<p align='center'>
    <a href='#-sobre'>Sobre</a> |
    <a href='#-projetos'>Projetos</a>
</p>

## 🤖 Sobre

Esse repositório consiste em um conjunto de projetos que submeti para completar a trilha de estudos back-end do [NADIC](https://nadic.ifrn.edu.br/). Existe nesse repositório um projeto de um banco de dados que foi baseado em um diagrama MER e convertido para MR e dois projetos com Django.

## 💻 Projetos

### Banco de dados REnter

Consiste em um banco de dados de uma locadora de carros que projetei o seu diagrama Modelo-Entidade-Relacionamento em um diagrama e depois o converti para um modelo relacional, utilizando MySQL.

Na sua pasta existe o diagrama REnter.png e um script SQL para migrar e popular o banco com dados iniciais.

Para o rodar siga os passos abaixo (é necessário ter o MySQL instalado):

```bash
# No MySQL CLI
CREATE DATABASE novo_banco_de_dados;

# No seu shell, seja linux/mac ou windows
# ./sql/
mysql -u seu_usuario -p novo_banco_de_dados < renter_dump.sql
```

### CRM (Web)

Consiste em um projeto web desenvolvido com o Django Framework, nele o usuário (sendo um funcionário) é capaz de gerenciar informações de uma locadora como carros, filiais, clientes e as próprias locações.

### CRM (API)

Consiste numa extensão do projeto anterior, foi feita com Django REST Framework e tive como objetivo apenas realizar um CRUD para cada aplicação, além disso, existem dois endpoints que só podem ser visualizados por staffs da empresa.

Para rodar ambos projetos, siga esses passos:

```bash

# Crie um virtual env dentro da pasta CRM
python -m venv .venv

# Ative-o (windows)
.venv\Scripts\Activate.ps1

# Ative-o (linux)
source .venv/bin/activate

# Instale as dependencias
pip install -r requirements.txt

# Migre os dados
python manage.py migrate

# Rode o projeto
python manage.py runserver
```

<p>Para acessar a versao web, basta ir até o <a href="http://localhost:8000/">http://localhost:8000/</a></p>
<p>Você pode visualizar os endpoints da API em <a href="http://localhost:8000/api/v1/swagger/">http://localhost:8000/api/v1/swagger/</a></p>
