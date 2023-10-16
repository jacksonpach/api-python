from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Importando seu modelo e metadata
from app.models.user import Base  # Ajuste esse import se o seu arquivo estiver em um módulo ou pacote diferente

# Metadata para o Alembic verificar as tabelas
target_metadata = Base.metadata

# Lendo configurações do alembic.ini
config = context.config

# Criando o engine a partir das configurações do alembic.ini
engine = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix="sqlalchemy.",
    poolclass=pool.NullPool,
)

# Configurando o contexto da migração para usar o engine criado
context.configure(
    connection=engine.connect(), target_metadata=target_metadata
)

# Iniciando a migração
with context.begin_transaction():
    context.run_migrations()
