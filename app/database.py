import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = os.getenv('DATABASE_URL', '').replace('mysql://', 'mysql+aiomysql://')

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def connect_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print('MySQL connected')

async def disconnect_db():
    await engine.dispose()
