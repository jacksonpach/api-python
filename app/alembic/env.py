from asyncio import run
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from app.config.settings import POSTGRES_URL  # Make sure this import reflects your project structure
# Import your model's MetaData and other necessary components
from app.models.user_model import Base  # Adjust to your project's structure

# Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Set the connection string from your configuration dynamically
config.set_main_option('sqlalchemy.url', POSTGRES_URL)

# Metadata object from your model's definition
target_metadata = Base.metadata
print(Base.metadata.tables)


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode with async engine."""
    # Here you would dynamically get your configuration from a settings file or environment variables
    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = POSTGRES_URL
    configuration['sqlalchemy.future'] = True

    # Create the async engine
    connectable = create_async_engine(
        configuration['sqlalchemy.url'],
        poolclass=pool.NullPool
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations, engine=connectable)


def do_run_migrations(connection: AsyncEngine, engine: AsyncEngine) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        version_table='alembic_version',
        render_as_batch=True,
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    pass
else:
    run(run_migrations_online())
