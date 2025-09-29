# 📈 TaskIQ Learning - API de Cotação de Moedas

Um projeto prático para aprender **TaskIQ** (task queue distribuído) construindo uma API que mantém atualizadas as cotações do dólar americano (USD) para real brasileiro (BRL) usando tarefas agendadas.

## 🎯 Objetivo

Construir uma API REST que:

- Retorna a cotação atual do USD→BRL consultando o banco de dados
- Mantém os dados atualizados automaticamente usando TaskIQ
- Demonstra conceitos de workers, schedulers e filas distribuídas

## 🏗️ Arquitetura

```markdown
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   FastAPI   │    │  Database   │    │   TaskIQ    │
│     API     │◄──►│  (SQLite)   │◄──►│ Scheduler   │
│             │    │             │    │ + Workers   │
└─────────────┘    └─────────────┘    └─────────▲───┘
                                                │
                                                ▼
                                      ┌─────────────┐
                                      │ AwesomeAPI  │
                                      │(External)   │
                                      └─────────────┘
```

### Componentes

- **API FastAPI**: Endpoints para consultar cotações
- **TaskIQ Scheduler**: Agenda tarefas para executar a cada minuto
- **TaskIQ Workers**: Processam as tarefas de atualização
- **Redis**: Message broker para filas de tarefas
- **SQLite**: Banco de dados local para armazenar cotações
- **AwesomeAPI**: API externa para obter cotações em tempo real

## 🚀 Como Executar

### 1. Pré-requisitos

```bash
# Python 3.13+
python --version

# Redis rodando (via Docker)
docker-compose up -d redis
```

### 2. Instalação

```bash
# Clonar repositório
git clone <repository-url>
cd taskiq-learning

# Instalar dependências
uv sync
```

### 3. Executar a aplicação

#### Opção A: Execução completa (3 terminais)

```bash
# Terminal 1 - API
python main.py
# Acesse: http://localhost:8080

# Terminal 2 - Scheduler (agenda tarefas)
make start-scheduler

# Terminal 3 - Worker (executa tarefas)
make start-worker
```

#### Opção B: Usando Docker para serviços

```bash
# Subir Redis
docker-compose up -d

# Seguir passos do Terminal 1, 2 e 3 acima
```

## 📋 Endpoints da API

### `GET /`

Página inicial da API

### `GET /currency/`

Retorna a última cotação armazenada no banco de dados

```json
{
  "id": 1,
  "code": "USD",
  "codein": "BRL", 
  "name": "Dólar Americano/Real Brasileiro",
  "high": 5.7340,
  "low": 5.7279,
  "bid": 5.7276,
  "ask": 5.7282,
  "timestamp": "2025-09-29T15:57:45",
  "create_date": "2025-09-29T15:57:45",
  "created_at": "2025-09-29T15:57:45",
  "updated_at": "2025-09-29T15:57:45"
}
```

### `GET /currency/latest`

Força a busca de uma nova cotação da API externa e retorna os dados atualizados

## ⚙️ Como o TaskIQ Funciona

### 1. **Scheduler** (`src/tasks.py`)

```python
@broker.task(schedule=[{"cron": "*/1 * * * *"}])
async def heavy_task() -> None:
    # Tarefa executada A CADA MINUTO
    # Busca cotação da AwesomeAPI
    # Atualiza banco de dados
```

### 2. **Componentes do TaskIQ**

#### **Broker (Message Queue)**

```python
broker = RedisStreamBroker("redis://localhost:6379")
```

- Responsável por receber e distribuir mensagens
- Usa Redis como backend de filas
- Gerencia a comunicação entre scheduler e workers

#### **Scheduler**

```python
scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)
```

- **Função**: Agenda tarefas baseadas em cron expressions
- **Executa**: `make start-scheduler`
- **O que faz**: A cada minuto, envia a tarefa `heavy_task` para a fila

#### **Worker**

```python
# Executado via CLI
taskiq worker src.tasks:broker
```

- **Função**: Processa tarefas da fila
- **Executa**: `make start-worker`  
- **O que faz**: Pega tarefas da fila e executa o código de atualização

### 3. **Fluxo de Execução**

```bash
Scheduler (a cada minuto)
    ↓ envia tarefa
Redis Queue
    ↓ worker pega tarefa
Worker executa heavy_task()
    ↓ busca dados
AwesomeAPI
    ↓ salva no banco
SQLite Database
    ↓ API consulta
FastAPI retorna dados
```

## 🛠️ Estrutura do Projeto

```bash
src/
├── api.py              # FastAPI app
├── tasks.py            # TaskIQ tasks, scheduler, broker
├── server.py           # Server startup
├── controllers/        # Business logic controllers
├── routes/             # API routes
├── services/           # External services (AwesomeAPI)
├── db/                 # Database models, repositories
├── schemas/            # Pydantic schemas
└── core/               # Settings, base classes

docker-compose.yml      # Redis service
Makefile               # Comandos úteis
```

## 🔧 Comandos Úteis

```bash
# Linting e formatação
make lint-fix

# TaskIQ
make start-scheduler    # Inicia scheduler
make start-worker      # Inicia worker

# Desenvolvimento
python main.py         # Inicia API
```

## 📊 Monitoramento

### Redis CLI

```bash
# Verificar filas
redis-cli keys "*taskiq*"

# Monitorar comandos
redis-cli monitor
```

### Logs

- **Scheduler**: Mostra quando tarefas são agendadas
- **Worker**: Mostra execução das tarefas e logs da aplicação
- **API**: Logs das requisições HTTP

## 🔄 Conceitos TaskIQ Demonstrados

1. **Scheduled Tasks**: Tarefas agendadas com cron
2. **Message Brokers**: Redis como broker de mensagens  
3. **Distributed Workers**: Workers processando tarefas em paralelo
4. **Result Backends**: Armazenamento de resultados das tarefas
5. **Async Tasks**: Tarefas assíncronas com SQLAlchemy async

## 📚 Tecnologias Utilizadas

- **TaskIQ**: Task queue distribuído
- **FastAPI**: Framework web moderno  
- **SQLAlchemy**: ORM assíncrono
- **Redis**: Message broker
- **Pydantic**: Validação de dados
- **SQLite**: Banco de dados
- **Docker**: Containerização de serviços

## 🎯 Próximos Passos

- [ ] Adicionar mais tipos de moeda (EUR, BTC)
- [ ] Implementar retry policy para falhas
- [ ] Adicionar métricas e monitoring
- [ ] Interface web para visualizar filas
- [ ] Testes automatizados
