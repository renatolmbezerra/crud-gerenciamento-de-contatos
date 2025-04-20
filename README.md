# 📇 Gerenciamento de Contatos

Sistema completo para **cadastro, acompanhamento e análise de interações com clientes**, projetado para otimizar o processo de vendas.

---

## 📌 Visão Geral

 O sistema permite o registro de contatos ativos (iniciados pela equipe) e receptivos (iniciados pelos clientes), com suporte para diversos canais de comunicação. Os dados são registrados em banco de dados e por fim consumidos por um painel do Power BI com metricas e KPIs para acompanhar o desempenho de cada operador.

---

## ✨ Funcionalidades

### 📝 Cadastro de Contatos

Tipos de contato:
- **Ativos**: iniciados pelo operador
- **Receptivos**: iniciados pelo cliente

Canais suportados:
- WhatsApp
- Ligação telefônica
- E-mail
- Visita presencial

### 🔄 Operações CRUD

- Adicionar novo contato  
- Visualizar lista de contatos  
- Obter detalhes de um contato  
- Editar informações  
- Remover contatos

### 📊 Dashboard Analítico

- Total de contatos e taxas de conversão  
- Análise de motivos de declínio  
- Desempenho por operador  
- Estatísticas por tipo de contato  

---

## 🛠️ Tecnologias Utilizadas

### Backend

- FastAPI  
- SQLAlchemy (ORM)  
- Uvicorn  
- Pydantic  

### Frontend

- Streamlit  
- Requests  
- Pandas  

### Infraestrutura

- Docker  
- PostgreSQL  
- Nginx  
- Digital Ocean  

---

## 🚀 Como Executar

### Pré-requisitos

- Docker Desktop  
- Instância do PostgreSQL (credenciais de acesso)

### Instalação

```bash
git clone [URL_DO_REPOSITORIO]
cd gerenciamento-contatos
docker-compose up -d
