# API de Álbuns Musicais Brasileiros

## Descrição

API REST simples para listar, adicionar, atualizar e remover álbuns musicais brasileiros.

## Pré-requisitos

  - Python 3.8+
  - pip

## Instalação e Execução

Este projeto pode ser executado localmente ou em um ambiente virtualizado e provisionado automaticamente, garantindo consistência e facilidade de configuração.

### Método 1: Localmente

Ideal para desenvolvimento rápido se você já possui o ambiente Python configurado.

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/laura-farias-dev/api-albuns-brasileiros.git
    cd api-albuns-brasileiros
    ```

2.  **Crie e ative o ambiente virtual:**

    ```bash
    python3 -m venv venv
    ```

      - No Windows: `venv\Scripts\activate`
      - No Linux/Mac: `source venv/bin/activate`

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a API:**

    ```bash
    python app.py
    ```

    A API estará acessível em `http://localhost:5000/api/albuns`.

-----

## Infraestrutura como Código (Vagrant + Ansible)

Para simular um ambiente mais próximo da produção e garantir um setup consistente, este projeto utiliza **Vagrant** para criar as máquinas virtuais e **Ansible** para automatizar a configuração do software.

### Método 2: Com Vagrant e Ansible (Recomendado)

Este método cria duas VMs para simular um ambiente cliente-servidor:

  - **vm1 (Nó de Controle):** Máquina de onde o Ansible é executado para configurar outros servidores.
  - **vm2 (Nó Gerenciado):** Máquina que é configurada pelo Ansible para rodar a API.

**Pré-requisitos:**

  - **VirtualBox:** [Download](https://www.virtualbox.org/wiki/Downloads)
  - **Vagrant:** [Download](https://www.vagrantup.com/downloads)

#### Passo 1: Iniciar as Máquinas Virtuais

No diretório raiz do projeto, execute o comando abaixo. O Vagrant irá criar as duas VMs e instalar o Ansible automaticamente na `vm1`.

```bash
vagrant up
```

#### Passo 2: Provisionar o Servidor com Ansible

Após as máquinas estarem no ar, vamos usar o Ansible (a partir da `vm1`) para instalar a aplicação na `vm2`.

1.  **Acesse o Nó de Controle (vm1):**

    ```bash
    vagrant ssh vm1
    ```

2.  **Execute o Playbook de Provisionamento:**
    Dentro da `vm1`, navegue até a pasta do projeto e execute o playbook. Os arquivos de configuração (`inventory.ini` e `configura-app.yaml`) já estão no repositório.

    ```bash
    # Navegue para a pasta compartilhada onde estão os arquivos do Ansible
    cd /vagrant

    # Execute o playbook
    ansible-playbook -i inventory.ini configura-app.yaml
    ```

    Aguarde o Ansible finalizar a configuração da `vm2`.

#### Passo 3: Executar e Testar a Aplicação

1.  **Inicie o servidor na vm2:**

      * Em um **novo terminal**, conecte-se à `vm2`: `vagrant ssh vm2`
      * Dentro da `vm2`, execute os comandos:
        ```bash
        # Navegue até a pasta que o Ansible clonou
        cd /home/vagrant/api-albuns-brasileiros

        # Ative o ambiente virtual que o Ansible criou
        source venv/bin/activate

        # Inicie o servidor Flask
        python app.py
        ```

2.  **Teste a API a partir da vm1:**

      * Volte para o terminal da `vm1` (ou abra um novo e conecte-se).
      * Execute o `curl` para testar a conexão:
        ```bash
        curl http://192.168.56.11:5000/api/albuns
        ```

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

### 1\. Workflow para Commits (push)

**Arquivo:** `.github/workflows/ci-push.yml`

```yaml
name: CI on Push

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

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
```

### 2\. Workflow para Pull Requests (pull\_request)

**Arquivo:** `.github/workflows/ci-pr.yml`

```yaml
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
```

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
    1.  Selecione o método **POST**.
    2.  Use a URL: `http://localhost:5000/api/albuns`
    3.  Na aba **Body**, escolha **raw** e selecione **JSON**.
    4.  Insira um JSON como:
        ```json
        {
          "nome": "Tropicália",
          "artista": "Caetano Veloso",
          "ano": 1968
        }
        ```
    5.  Clique em **Send**.
        A resposta será o álbum criado, com um novo `id`.

### Atualizar álbum (PUT)

  - **Endpoint:** `/api/albuns/<album_id>`
  - **Método:** PUT
  - **Descrição:** Atualiza os dados de um álbum existente.
  - **Exemplo de uso no Postman:**
    1.  Selecione o método **PUT**.
    2.  Use a URL: `http://localhost:5000/api/albuns/1`
    3.  Na aba **Body**, escolha **raw** e selecione **JSON**.
    4.  Insira o JSON com os campos a atualizar:
        ```json
        {
          "nome": "Clube da Esquina 2",
          "artista": "Milton Nascimento",
          "ano": 1978
        }
        ```
    5.  Clique em **Send**.
        A resposta será o álbum já atualizado.

### Remover álbum (DELETE)

  - **Endpoint:** `/api/albuns/<album_id>`
  - **Método:** DELETE
  - **Descrição:** Remove um álbum pelo seu `id`.
  - **Exemplo de uso no Postman:**
    1.  Selecione o método **DELETE**.
    2.  Use a URL: `http://localhost:5000/api/albuns/1`
    3.  Clique em **Send**.
        A resposta confirmará a remoção, retornando uma mensagem e o álbum excluído.
