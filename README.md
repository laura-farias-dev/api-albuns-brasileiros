# API de Álbuns Musicais Brasileiros

## Descrição
API REST simples para listar, adicionar, atualizar e remover álbuns musicais brasileiros.

## Pré-requisitos
- Python 3.8+
- pip

## Instalação e execução

### Clone o repositório
1. git clone https://github.com/<seu-usuario>/api-albuns-brasileiros.git  
2. cd api-albuns-brasileiros

### Crie e ative o ambiente virtual
1. python3 -m venv venv  
2. source venv/bin/activate  # Linux/Mac  
3. venv\Scripts\activate     # Windows

### Instale as dependências
- pip install -r requirements.txt

### Execute a API
- python app.py  

Acesse: [http://localhost:5000/api/albuns](http://localhost:5000/api/albuns)

## Workflow Utilizado
Este projeto utiliza o Github Flow como estratégia de controle de versão.
O Github Flow é um fluxo de trabalho simples e direto, recomendado para projetos com uma única versão em produção, como APIs simples, sites e blogs.
Neste fluxo, todo desenvolvimento parte da branch principal (main), e cada nova funcionalidade ou correção é feita em uma branch separada, sendo mesclada à main após revisão. Isso facilita deploys frequentes e mantém o código de produção sempre atualizado.

### Por que escolhi o Github Flow?

O projeto é simples, com uma única versão em produção.
Permite adicionar e revisar novas funcionalidades de forma rápida.
Facilita o controle e a colaboração, mesmo em equipes pequenas.

## Integração Contínua com GitHub Actions

Este repositório inclui dois fluxos de trabalho automáticos para validar todo push e pull request na branch `main`.

### 1. Workflow para Commits (push)
**Arquivo:** `.github/workflows/ci-push.yml`

name: CI on Push

on:
push:
branches:
- main

jobs:
build:
runs-on: ubuntu-latest

text
steps:
  - name: Clonar repositório e trocar para a branch
    uses: actions/checkout@v4
    with:
      ref: main

  - name: Instalar Python
    uses: actions/setup-python@v5
    with:
      python-version: '3.10'

  - name: Instalar dependências
    run: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt


  - name: Executar aplicação para teste rápido
    run: |
      nohup python app.py &
      sleep 5
      curl --fail http://localhost:5000/api/albuns
text

### 2. Workflow para Pull Requests (pull_request)
**Arquivo:** `.github/workflows/ci-pr.yml`

name: CI on Pull Request

on:
pull_request:
branches:
- main
types:
- opened
- synchronize
- reopened

jobs:
build:
runs-on: ubuntu-latest

text
steps:
  - name: Clonar repositório e trocar para a branch do PR
    uses: actions/checkout@v4
    with:
      ref: ${{ github.event.pull_request.head.ref }}

  - name: Instalar Python
    uses: actions/setup-python@v5
    with:
      python-version: '3.10'

  - name: Instalar dependências
    run: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt

  - name: Executar aplicação para teste rápido
    run: |
      nohup python app.py &
      sleep 5
      curl --fail http://localhost:5000/api/albuns
text

## Rotas da API

### Listar álbuns (GET)
- **Endpoint:** `/api/albuns`  
- **Método:** GET  
- **Descrição:** Retorna a lista de álbuns musicais brasileiros.  
- **Exemplo de uso:**  
  Acesse `http://localhost:5000/api/albuns` pelo navegador ou pelo Postman.

### Adicionar álbum (POST)
- **Endpoint:** `/api/albuns`  
- **Método:** POST  
- **Descrição:** Adiciona um novo álbum à lista.  
- **Exemplo de uso no Postman:**  
  1. Selecione o método **POST**.  
  2. Use a URL: `http://localhost:5000/api/albuns`  
  3. Na aba **Body**, escolha **raw** e selecione **JSON**.  
  4. Insira um JSON como:
     ```
     {
       "nome": "Tropicália",
       "artista": "Caetano Veloso",
       "ano": 1968
     }
     ```
  5. Clique em **Send**.  
     A resposta será o álbum criado, com um novo `id`.

### Atualizar álbum (PUT)
- **Endpoint:** `/api/albuns/<album_id>`  
- **Método:** PUT  
- **Descrição:** Atualiza os dados de um álbum existente.  
- **Exemplo de uso no Postman:**  
  1. Selecione o método **PUT**.  
  2. Use a URL: `http://localhost:5000/api/albuns/1`  
  3. Na aba **Body**, escolha **raw** e selecione **JSON**.  
  4. Insira o JSON com os campos a atualizar:
     ```
     {
       "nome": "Clube da Esquina 2",
       "artista": "Milton Nascimento",
       "ano": 1978
     }
     ```
  5. Clique em **Send**.  
     A resposta será o álbum já atualizado.

### Remover álbum (DELETE)
- **Endpoint:** `/api/albuns/<album_id>`  
- **Método:** DELETE  
- **Descrição:** Remove um álbum pelo seu `id`.  
- **Exemplo de uso no Postman:**  
  1. Selecione o método **DELETE**.  
  2. Use a URL: `http://localhost:5000/api/albuns/1`  
  3. Clique em **Send**.  
     A resposta confirmará a remoção, retornando uma mensagem e o álbum excluído.

---

Agora, toda modificação na branch `main`, seja via commit ou pull request, disparará validações automáticas que clonam o repositório, instalam o interpretador e dependências e executam a API.