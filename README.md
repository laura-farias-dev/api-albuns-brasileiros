# API de Álbuns Musicais Brasileiros

## Descrição
API REST simples para listar e adicionar álbuns musicais brasileiros.

## Pré-requisitos
- Python 3.8+
- pip

## Instalação e execução

### Clone o repositório
1. git clone https://github.com/<seu-usuario>/api-albuns-brasileiros.git
2. cd api-albuns-brasileiros

### Crie e ative o ambiente virtual
1. python3 -m venv venv
2. source venv/bin/activate # Linux/Mac
3. venv\Scripts\activate # Windows

### Instale as dependências
- pip install flask

### Execute a API
- python app.py

Acesse: [http://localhost:5000/api/albuns](http://localhost:5000/api/albuns)

---

## Workflow Utilizado

Este projeto utiliza o **Github Flow** como estratégia de controle de versão.  
O Github Flow é um fluxo de trabalho simples e direto, recomendado para projetos com uma única versão em produção, como APIs simples, sites e blogs.  
Neste fluxo, todo desenvolvimento parte da branch principal (`main`), e cada nova funcionalidade ou correção é feita em uma branch separada, sendo mesclada à `main` após revisão. Isso facilita deploys frequentes e mantém o código de produção sempre atualizado.

**Por que escolhi o Github Flow?**
- O projeto é simples, com uma única versão em produção.
- Permite adicionar e revisar novas funcionalidades de forma rápida.
- Facilita o controle e a colaboração, mesmo em equipes pequenas.

---

## Rotas da API

### Listar álbuns (GET)
- **Endpoint:** `/api/albuns`
- **Método:** GET
- **Descrição:** Retorna a lista de álbuns musicais brasileiros.
- **Exemplo de uso:**  
  Acesse [http://localhost:5000/api/albuns](http://localhost:5000/api/albuns) pelo navegador ou pelo Postman.

### Adicionar álbum (POST)
- **Endpoint:** `/api/albuns`
- **Método:** POST
- **Descrição:** Adiciona um novo álbum à lista.
- **Exemplo de uso no Postman:**
  1. Selecione o método **POST**.
  2. Use a URL: `http://localhost:5000/api/albuns`
  3. Na aba **Body**, escolha **raw** e selecione **JSON**.
  4. Insira um JSON como, por exemplo:
     ```
     {
       "nome": "Tropicália",
       "artista": "Caetano Veloso",
       "ano": 1968
     }
     ```
  5. Clique em **Send**.  
     A resposta será o álbum criado, com um novo `id`.
