from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from config.config import settings


SQLALCHEMY_DATABASE_URL = settings.get_database_url
engine = create_async_engine(SQLALCHEMY_DATABASE_URL,
                             echo=settings.DEBUG,
                             pool_pre_ping=True,
                             pool_recycle=3600,)


async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    """Dependency for getting async session"""

    async with async_session() as session:
        try:
            yield session
        except: # noqa
            raise Exception("failed to get session")
