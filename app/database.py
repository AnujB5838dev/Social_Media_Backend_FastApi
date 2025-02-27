from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

from urllib.parse import quote      #ye issiliye kiya kyu ki apne password me @ hai issiliye parsing me problem ho rhi thi
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time





encoded_password = quote(settings.database_password)  # Output: "aA%409765249523"



# SQLALCHEMY_DATABASE_URL = "postresql://<username>:<password>@<ip-address or hostname>/<database_name>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{encoded_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:

#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='aA@9765249523',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()    #used for query execution
#         print("Connection to database was successful")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error was : ", error)
#         time.sleep(2)

