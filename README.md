# Bookshare
Aplicativo de gerenciamento e compartilhamente de livros, a partir
de bibliotecas criadas pelos usuários e o compartilhamento destas com seus
amigos.

Este projeto é parte componente avaliativa da disciplina de
EECP0036 - Desenvolvimento de Sistemas Web (2024.2)

## Alunos:
[Ernamilson Rezende](https://github.com/ern4m)

[Vinicius Santos]()

## Instalação
- Requisitos:
    - Python 3.13 (creio que versões anteriores devam funcionar sem problemas de compatibilidade);
    - SQLite.
- Instruções:
    - ```git clone https://github.com/ern4m/bookshare.git``` ou
     ```git clone git@github.com:ern4m/bookshare.git```
    - ```cd bookshare```
    - Substitua `SECRET_KEY` em `config.py` por uma chave segura.
    - Crie um ambiente virtual e ative ele
    - Instale as dependencias 
    ```pip install -r requirements.txt```
    - Faça a população do banco, se desejar com o comando: 
    ```flask populate-db```
    - Inicie o projeto com o comando:
    ```python run.py```
