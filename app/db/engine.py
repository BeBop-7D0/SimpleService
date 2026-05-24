from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
from os import getenv

load_dotenv()
protocol = "postgresql+asyncpg://"
user = getenv("POSTGRES_USER")
password = getenv("POSTGRES_PASSWORD")
db = getenv("POSTGRES_DB")

DATABASE_URL = f"{protocol}{user}:{password}@localhost:5432/{db}"

async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

async_sessionmaker = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
)

