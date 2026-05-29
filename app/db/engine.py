from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker as make_session

from dotenv import load_dotenv
from os import getenv
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent.parent / "docker" / ".env"
load_dotenv(env_path)
protocol = "postgresql+asyncpg://"
user = getenv("POSTGRES_USER")
password = getenv("POSTGRES_PASSWORD")
db = getenv("POSTGRES_DB")

DATABASE_URL = f"{protocol}{user}:{password}@localhost:5432/{db}"

engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

async_session_factory = make_session(
    engine,
    expire_on_commit=False
)
