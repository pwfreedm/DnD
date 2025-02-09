from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class DB_Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=DB_Base)

def count_rows (cl_name: object) -> int:
    return db.session.query(cl_name).count()


