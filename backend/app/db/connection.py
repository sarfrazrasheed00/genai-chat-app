from sqlalchemy import create_engine, text

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL.replace(
        "postgresql://", "postgresql+psycopg://", 1
    ),
    pool_pre_ping=True
)

def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("[DEBUG] Database result:", result.scalar())
        print("[SUCCESS] PostgreSQL connected!")

if __name__ == "__main__":
    test_connection()