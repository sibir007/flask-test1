import email
import enum
from pydoc import doc
from ssl import DER_cert_to_PEM_cert
import sqlalchemy
import sqlalchemy.orm
from src.db import db, intpk, timstamp, utc_timstamp, required_name
from typing import List, Literal, Optional
from sqlalchemy import ForeignKey, String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from src import admin, bcrypt

class Status(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'

# Status = Literal['user', 'admin']

class Admin(UserMixin, db.Model):
    # __bind_key__ = 'admin'
    
    
    id: Mapped[intpk]
    created_at: Mapped[utc_timstamp]
    name: Mapped[required_name] = mapped_column(unique=True)
    full_name: Mapped[Optional[str]]
    password: Mapped[str]
    # password: Mapped[str] = mapped_column(d=lambda pw: bcrypt.generate_password_hash(pw))
    addresses: Mapped[List['Address']] = relationship(back_populates='admin', 
                                                      cascade="all, delete-orphan",
                                                      doc='some doc')
    # status: Mapped[Status]
    # status: Mapped[Status] = mapped_column(
    #     sqlalchemy.Enum("pending", "received", "completed", name="status_enum")
    # )
    
    
    def __repr__(self) -> str:
        return f"Admin(id={self.id}, username={self.adminname})"
    
class Address(db.Model):
    
    id: Mapped[intpk]
    email_address: Mapped[str]
    admin_id = mapped_column(ForeignKey('admin.id'))

    admin: Mapped[Admin] = relationship(back_populates='addresses')
    
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    
    