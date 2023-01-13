from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (f'postgresql://'
                '{db_user}:{db_password}'
                '@{db_host}:{db_port}/{db_name}')


engine = create_engine(DATABASE_URL, echo=True)
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
