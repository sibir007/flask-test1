import sqlalchemy
import sqlalchemy.orm
from src import db
from typing import List, Optional
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from src import bcrypt


class User(UserMixin, db.Model):
    __bind_key__ = 'admin'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(d=lambda pw: bcrypt.generate_password_hash(pw))
    
    sqlalchemy.orm.
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username})"