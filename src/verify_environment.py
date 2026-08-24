from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://dss150p:dss150p_lab@127.0.0.1:5432/dss150p_lab"
)

with engine.connect() as conn:
    print(conn.execute(text("SELECT version();")).scalar())
    print(conn.execute(text("SELECT current_database();")).scalar())