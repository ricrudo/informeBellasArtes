from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

from os import environ

# si no se declara el nombre de la base de datos en las variables de entorno se trabaja con al base de datos "bellasartes_test"
name_db = environ.get('NAME_DB', 'bellasartes_test.sqlite?charset=utf8')

engine = create_engine(f'sqlite:///{name_db}.sqlite', echo=True, poolclass=NullPool)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


from app.interface.db.person_exists import is_real_person

