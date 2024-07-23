from ..db import (
    db, intpk, timstamp, 
    utc_timstamp, required_name,
    PkCereatedAtUTCMixin, PkMixin,
    PkCereatedAtMixin
                    )


import click
from typing import List, Literal, Optional
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship,
    validates
    )
from flask_security import UserMixin, RoleMixin, hash_password, Security

# class Status(enum.Enum):
#     USER = 'user'
#     ADMIN = 'admin'

# Status = Literal['user', 'admin']







# class AdminRole(PkMixin, db.Model):
#     """таблица асоциативности админ-роль"""
    
#     __bind_key__ = 'admin'
#     __tablename__ = 'admin_role'
    
#     my_admin_id: Mapped[int]  = mapped_column(ForeignKey('my_admin.id'), primary_key=True)
#     role_id: Mapped[int] = mapped_column(ForeignKey('role.id'), primary_key=True)

class MyAdmin(PkCereatedAtMixin, UserMixin, db.Model):
    # __bind_key__ = 'admin'
    # __tablename__ = 'my_admin'
    # __tablename__ = 'admin'
    
    
    # name: Mapped[required_name] = mapped_column(unique=True)
    # full_name: Mapped[Optional[str]]
    password: Mapped[str]
    # password: Mapped[str] = mapped_column(d=lambda pw: bcrypt.generate_password_hash(pw))
    
    email: Mapped[str]
    
    phones: Mapped[List['Telephone']] = relationship(
        back_populates='admin',
        cascade="all, delete-orphan",
        doc='some doc'
    )
    active: Mapped[Optional[bool]]
    
    roles: Mapped[List['Role']] = relationship(
        secondary='admin_role', back_populates='my_admins'
    )
    
    fs_uniquifier: Mapped[str] = mapped_column(unique=True)
    
    @validates('password')                                                 
    def hashing_password(self, key, password):
        return hash_password(password)
    # status: Mapped[Status]
    # status: Mapped[Status] = mapped_column(
    #     sqlalchemy.Enum("pending", "received", "completed", name="status_enum")
    # )
    
    def __repr__(self) -> str:
        return f"MyAdmin(id={self.id}, username={self.name})"
    
    
class Telephone(PkMixin, db.Model):
    # __bind_key__ = 'admin'
    # __tablename__ = 'address'
    
    telephone: Mapped[str]

    my_admin_id: Mapped[int] = mapped_column(ForeignKey('my_admin.id'))

    admin: Mapped['MyAdmin'] = relationship(back_populates='phones')
    
    def __repr__(self) -> str:
        return f"Telephone(id={self.id!r}, email_address={self.telephone!r})"

    
class Role(PkMixin, RoleMixin, db.Model):
    """таблица раолей админов для организации доступа
    к администрируемым сущьностям"""
    
    # __bind_key__ = 'admin'
    __tablename__ = 'role'
    
    name: Mapped[required_name]
    description: Mapped[Optional[str]]
    
    my_admins: Mapped[List['MyAdmin']] = relationship(
        secondary='admin_role', back_populates='roles'
    )
    
    
admin_role = db.Table(
    'admin_role',
    db.Model.metadata,
    Column('role_id', ForeignKey('role.id'), primary_key=True),
    Column('my_admin_id', ForeignKey('my_admin.id'), primary_key=True),
    # bind_key='admin'
)



    