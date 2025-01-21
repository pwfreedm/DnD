from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class DB_Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=DB_Base)

