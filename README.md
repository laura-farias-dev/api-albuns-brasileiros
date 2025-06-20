# API de Álbuns Musicais Brasileiros

## Descrição

API REST simples para listar, adicionar, atualizar e remover álbuns musicais brasileiros. Este projeto inclui um ambiente de desenvolvimento virtualizado com Vagrant para garantir consistência e facilidade de configuração, além de um pipeline de Integração Contínua com GitHub Actions para validação automática.

## Instalação e Execução

Você pode executar este projeto de duas maneiras: localmente na sua máquina ou dentro de um ambiente virtualizado com Vagrant.

### Método 1: Localmente (Na sua máquina)

Este método é ideal para desenvolvimento rápido se você já possui o ambiente Python configurado.

**Pré-requisitos:**

  - Python 3.8+
  - pip

**Passos:**

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

### Método 2: Com Vagrant (Ambiente Virtualizado Recomendado)

Este método cria duas máquinas virtuais para simular um ambiente de cliente-servidor, garantindo que a aplicação rode em um ambiente limpo e consistente, independentemente do seu sistema operacional.

**Pré-requisitos Adicionais:**

  - **VirtualBox:** [Download](https://www.virtualbox.org/wiki/Downloads)
  - **Vagrant:** [Download](https://www.vagrantup.com/downloads)

**Estrutura da Infraestrutura:**
O Vagrant provisiona duas máquinas virtuais com Ubuntu:

  * **vm2 (Servidor):**
      * **IP:** `192.168.56.11`
      * Executa a API Flask.
  * **vm1 (Cliente):**
      * **IP:** `192.168.56.10`
      * Usada para simular um cliente e testar o acesso à API.

**Passos:**

1.  **Inicie a infraestrutura:**
    No diretório raiz do projeto (onde está o `Vagrantfile`), execute:

    ```bash
    vagrant up
    ```

    Este comando irá baixar o sistema operacional, criar as duas VMs, instalar as dependências do Python e iniciar a API na `vm2` automaticamente.

2.  **Teste a API a partir do cliente:**
    Para confirmar que tudo está funcionando, acesse a `vm1` e faça uma requisição para a `vm2`.

    ```bash
    # Conecte-se à VM cliente
    vagrant ssh vm1

    # Dentro da vm1, use o curl para testar a API na vm2
    curl http://192.168.56.11:5000/api/albuns
    ```

    A saída esperada é o JSON com a lista de álbuns.

**Gerenciamento do Ambiente Vagrant:**

  * **Desligar as VMs:** `vagrant halt`
  * **Ligar as VMs:** `vagrant up`
  * **Destruir as VMs (apaga tudo):** `vagrant destroy -f`
  * **Verificar o status:** `vagrant status`

## Rotas da API

  - **URL Base Local:** `http://localhost:5000`
  - **URL Base via Vagrant (testando de fora da VM):** Acesso via `localhost` é possível com `port forwarding`, mas o teste principal é feito entre as VMs.

### Listar álbuns (GET)

  - **Endpoint:** `/api/albuns`
  - **Exemplo de uso:** `http://localhost:5000/api/albuns`

### Adicionar álbum (POST)

  - **Endpoint:** `/api/albuns`
  - **Exemplo de Corpo (Body) JSON:**
    ```json
    {
      "nome": "Tropicália",
      "artista": "Caetano Veloso",
      "ano": 1968
    }
    ```

### Atualizar álbum (PUT)

  - **Endpoint:** `/api/albuns/<album_id>`
  - **Exemplo de Corpo (Body) JSON:**
    ```json
    {
      "nome": "Clube da Esquina 2",
      "ano": 1978
    }
    ```

### Remover álbum (DELETE)

  - **Endpoint:** `/api/albuns/<album_id>`

## Workflow Utilizado

Este projeto utiliza o Github Flow como estratégia de controle de versão. O Github Flow é um fluxo de trabalho simples e direto, recomendado para projetos com uma única versão em produção.
Neste fluxo, todo desenvolvimento parte da branch principal (`main`), e cada nova funcionalidade ou correção é feita em uma branch separada, sendo mesclada à `main` após revisão.

## Integração Contínua com GitHub Actions

Este repositório inclui fluxos de trabalho automáticos (`.github/workflows/`) para validar todo `push` e `pull_request` na branch `main`. Os workflows instalam as dependências e executam um teste rápido na API para garantir a integridade do código.