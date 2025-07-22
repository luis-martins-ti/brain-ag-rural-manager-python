# 🌾 Rural Manager API

API REST para gerenciar produtores rurais, propriedades, safras e colheitas.

Validação de CPF/CNPJ
Autenticação JWT
Dashboard com KPIs e gráficos
Banco de dados PostgreSQL
Docker para orquestração
Testes unitários e integrados

---

## 🚀 Como iniciar o projeto

### ✅ Pré-requisitos
- Docker + Docker Compose

---

### 🧱 STEP 1 - Build e start com Docker

**Renomeie o arquivo .env.example para .env e execute:**

```bash
docker compose build --no-cache
docker compose up -d
```

### 📦 STEP 2 - Criar banco e aplicar migrações SqlAlchemy + 

As migrações rodam automaticamente ao inicializar a aplicação com Docker. Aguarde alguns segundos.
Se desejar criar uma massa de dados para testes, basta rodar o seed:
```bash
docker-compose exec web python app/db/seed.py
```

### 🖥️ STEP 3 - Iniciar a aplicação
A aplicação se inicia automaticamente com o Docker após alguns segundos. Para acessar a API use: http://localhost:8000/

### 📚 DOCUMENTAÇÃO:
Acesse a documentação interativa no navegador:
```bash
 http://localhost:8000/docs
```
Na raiz do projeto existe o arquivo swagger.json para uso nos testes das requisições. Ajuste para usar Bearer Token na Autenticação.
Se preferir, existe o arquivo **Rural API.postman_collection** já configurado para usar o token do login de forma automática nas rotas.
Para exportar o swagger.json:
```bash
curl http://localhost:8000/openapi.json -o swagger.json
```

**Como usar swagger.json no Postman / Insomnia**
Swagger UI:

Acesse: https://editor.swagger.io/
Clique em "File" → "Import File" → selecione swagger.json

Postman:

Vá em Import > File > Upload Files > swagger.json
Os endpoints serão importados automaticamente.

Insomnia:

Vá em Create > Import From File > swagger.json
Ele criará uma collection pronta para testar a API.


### 🧪 TESTES:
Rodar fora do container:

```bash
docker-compose exec web pytest app/tests
```
**Estrutura usada para testes:**
Testes estão localizados na pasta tests
Usa Pytest para simular requisições HTTP reais
Logs e observações via terminal:
```bash
docker-compose logs -f web
```

### 📘 Tecnologias Utilizadas
- Python 3.10+
- FastAPI
- SQLAlchemy + Alembic
- PostgreSQL
- Docker & Docker Compose
- Pytest para testes

### Arquitetura:
rural_api/
├── app/
│   ├── api/                  # Rotas
│   ├── auth/                 # Autenticação JWT
│   ├── core/             	  # Configurações    
│   ├── db/              	    # Models e database
│   ├── schemas/              # Pydantic Validations
│   ├── services/         	  # Lógica de negócio	
│   └── tests/                # Testes
├── Dockerfile
├── docker-compose.yml
├── .env
├── requirements.txt
└── README.md

**Para encerrar a aplicação basta executar:**
```bash
docker compose down -v --remove-orphans
```