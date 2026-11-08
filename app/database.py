from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import make_url
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL

database_url = make_url(DATABASE_URL)

if database_url.drivername == "sqlite":
    engine = create_engine(
        database_url,
        connect_args={"check_same_thread": False}
    )
elif database_url.drivername == "postgresql":
    # SQLAlchemy 2.1 defaults plain PostgreSQL URLs to psycopg 3.
    # This project installs psycopg2-binary, so select that driver explicitly.
    engine = create_engine(database_url.set(drivername="postgresql+psycopg2"))
else:
    engine = create_engine(database_url)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()