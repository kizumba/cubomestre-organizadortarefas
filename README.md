# Atualização do CRUD
|Entidade|Create|Read|Update|Delete|
|---|---|---|---|---|
|Funcionário|X|X|X|X|
|Tipo de Funcionário|X|X|X|X|
|Cliente|X|X|X|X|
|Habilidade|X|X|X|X|
|Projeto|-|-|-|-|
|Tarefa|-|-|-|-|

# Cubo Mestre
Primeiro projeto da empresa Cubo Mestre. Projeto piloto para desenvolver as habilidades pessoais e em grupo. O foco é desenvolver uma aplicação para gerenciar projetos segmentando-o em partes menores chamadas de tarefas. Cada Tarefa pode ser executada por um, e somente um, colaborador.

## Teste de edição no github
- [x] Alteração Teste(Edu)
- [ ] Alteração Eder
- [x] Alteração André

# Ferramentas
## Backend
* Python - linguagem de programação de porpósito geral. https://www.python.org/
* Django - framework para construção full-stack - https://www.djangoproject.com/

## Frontend
* HTML
* CSS
* JS

## IDE
* Visual Code
* PyCharm

## Documentação 
* Markdown - usando para escrever a documentação - https://docs.pipz.com/central-de-ajuda/learning-center/guia-basico-de-markdown#open

# Instalando e configurando o ambiente de desenvolvimento
## Git 
* `git init` para iniciar o repositório
* `git clone` para clonar o repositório
* `git status` para verificar aletações nos arquivos
* `git add .` para adicionar os arquivos no stage
* `git commit -m "mensagem"` para commitar os arquivos
* `git push` para enviar para o github

## Ambiente virtual
* `python3 -m venv venv` para criar o ambiente virtual de desenvolvimento
* `source venv/bin/activate` para ativar o ambiente
* `deactivate` para desativar
* `pip freeze > requirements.txt` gerar arquivo com as dependências do projeto. Sempre usar depois de instalar uma nova biblioteca.
* `pip install -r requirements.txt` instalar todas as dependências do arquivo.

## Django
### Instalações
* `pip install django` para instalar o Django
* `pip install django-bootstrap4` para usar css direto no projeto.

### Projeto
* `django-admin startproject <nome>` criar projeto
* `python manage.py startapp <nome>` criar aplicação

# Projeto001 - Organizador de Tarefas
## Criando projeto django
Para criar um projeto Django utilizamos o comando `django-admin startproject setup .`, normalmente utiliza-se o nome **setup** para o nome do projeto. Nesta pasta ficará os arquivos responsáveis pelas configurações do projeto. O . no final do nome significa criar o projeto na pasta atual. Sem o . o projeto ficará dentro de outra pasta.

## Criando super usuário
* `python manage.py createsuperuser` nome admin, senha a@1234, email -

## Criando a aplicação
Para criar uma aplicação para gerar funcionalidades ao projeto, utilizamos o comando `python manage.py startapp app`, lembrando que app pode ser qualquer nome significativo.

Este projeto concentrará todos os models no mesmo app, assim não será necessário dar um nome melhor.

## Configurando o arquivo settings.py
Dentro da pasta **setup** abrir o arquivo **settings.py**, adicionar nossa **app** na variável INSTALLED_APPS.

Alterar a variável LANGUAGE_CODE para pt-br. Alterar a variável TIME_ZONE para America/Sao_Paulo.

## Testando servidor
Utilizar o comando `python manage.py runserver` para rodar a aplicação, se tudo ocorrer bem, a página padrão do django será mostrada.

## Banco de dados
No Django existem dois comandos essenciais para interagir com banco de dados. O primeiro comando é o `python manage.py makemigrations` que diz ao django todos os modelos e alterações nos modelos que façamos.

O outro comando é o `python manage.py migrate` que diz ao django para executarmos as mudanças.

# Git Desenvolvimento

## Branchs
* main
* funcionario

