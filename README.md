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
