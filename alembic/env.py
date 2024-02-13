from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from dotenv import load_dotenv

from app.database.database import Base
import os

load_dotenv()

config = context.config

database_url = os.getenv("URL_DATABASE")
config.set_main_option('sqlalchemy.url', database_url)

fileConfig(config.config_file_name)

target_metadata = Base.metadata

config.attributes['connection'] = context.get_x_argument(as_dictionary=True).get(
    'sqlalchemy.url',
    database_url
)

engine = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix='sqlalchemy.',
    poolclass=pool.NullPool,
)
connection = engine.connect()

context.configure(
    connection=connection,
    target_metadata=target_metadata
)

with context.begin_transaction():
    context.run_migrations()
