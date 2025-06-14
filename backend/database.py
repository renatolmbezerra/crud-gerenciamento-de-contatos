from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pathlib import Path
from urllib.parse import quote_plus  # Importação adicionada

def load_settings():
    """Carrega as configurações a partir de variáveis de ambiente."""
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_pass": os.getenv("POSTGRES_PASSWORD"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_port": os.getenv("POSTGRES_PORT"),
        "db_ssl": os.getenv("POSTGRES_SSLMODE"),
    }

    # Valida se todas as variáveis de ambiente foram carregadas
    for key, value in settings.items():
        if value is None:
            raise ValueError(f"Variável de ambiente faltando: {key}")
        
    return settings

settings = load_settings()

# Escapa caracteres especiais na senha
password = quote_plus(settings['db_pass'])

# Monta a string de conexão do banco de dados
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings['db_user']}:{password}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}?sslmode={settings['db_ssl']}"

# Cria o motor do banco de dados, é a conexão com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão de banco de dados, é quem vai executar as queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Teste de conexão com o banco de dados
# Este bloco de código é executado apenas se o arquivo for executado diretamente
if __name__ == "__main__":
    print("Testando conexão com o banco de dados...")
    try:
        conn = engine.connect()
        conn.execute(text("SELECT 1"))
        print("✅ Conexão bem-sucedida!")
        conn.close()
    except Exception as e:
        print(f"❌ Falha na conexão: {str(e)}")