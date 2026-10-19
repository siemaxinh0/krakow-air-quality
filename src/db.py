import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

def get_engine():
    load_dotenv()
    password = os.getenv("POSTGRES_PASSWORD")
    address = f'postgresql+psycopg://postgres:{password}@localhost:5433/postgres'
    engine = create_engine(address, connect_args={"connect_timeout": 5})
    return engine
