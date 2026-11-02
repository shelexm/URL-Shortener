from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from collections.abc import AsyncIterator
from app.config.config import settings
from fastapi import Request

def create_engine(settings: settings) -> AsyncEngine:
    return create_async_engine(settings.database_url,
    echo=True)


def create_sessionmaker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine)


async def get_session(request: Request) -> AsyncIterator[AsyncSession]:
    sessionmaker: async_sessionmaker[AsyncSession] - request.app.state.sessionmaker
    async with sessionmaker() as session:
        yield session

