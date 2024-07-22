from src.db import (
    db, intpk, timstamp, 
    utc_timstamp, required_name,
    PkCereatedAtUTCMixin, PkMixin
                    )

import click
from flask import Flask, current_app
from typing import List, Literal, Optional
from sqlalchemy import ForeignKey, String, Integer, Float, Table
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship,
    validates
    )
from flask_security import UserMixin, RoleMixin, hash_password, Security

# class Status(enum.Enum):
#     USER = 'user'
#     ADMIN = 'admin'

# Status = Literal['user', 'admin']

class Admin(PkCereatedAtUTCMixin, UserMixin, db.Model):
    __bind_key__ = 'admin'
    # __tablename__ = 'admin'
    
    
    name: Mapped[required_name] = mapped_column(unique=True)
    # full_name: Mapped[Optional[str]]
    password: Mapped[str]
    # password: Mapped[str] = mapped_column(d=lambda pw: bcrypt.generate_password_hash(pw))
    
    email: Mapped[str]
    
    phones: Mapped[List['Telephone']] = relationship(
        back_populates='admin',
        cascade="all, delete-orphan",
        doc='some doc'
    )
    
    @validates('password')                                                 
    def hashing_password(self, key, password):
        return hash_password(password)
    # status: Mapped[Status]
    # status: Mapped[Status] = mapped_column(
    #     sqlalchemy.Enum("pending", "received", "completed", name="status_enum")
    # )
    roles: Mapped[List['Role']] = relationship(
        secondary='admin_role', back_populates='admins'
    )
    
    
    def __repr__(self) -> str:
        return f"Admin(id={self.id}, username={self.adminname})"
    
    
class Telephone(PkMixin, db.Model):
    __bind_key__ = 'admin'
    # __tablename__ = 'address'
    
    telephone: Mapped[str]

    admin_id: Mapped[int] = mapped_column(ForeignKey('admin.id'))

    admin: Mapped['Admin'] = relationship(back_populates='phones')
    
    def __repr__(self) -> str:
        return f"Telephone(id={self.id!r}, email_address={self.telephone!r})"

    
class Role(PkMixin, RoleMixin, db.Model):
    """таблица раолей админов для организации доступа
    к администрируемым сущьностям"""
    
    __bind_key__ = 'admin'
    
    role: Mapped[required_name]
    description: Mapped[Optional[str]]
    
    admins: Mapped[List['Admin']] = relationship(
        secondary='admin_role', back_populates='roles'
    )
    
    

class AdminRole(PkMixin, db.Model):
    """таблица асоциативности админ-роль"""
    
    __bind_key__ = 'admin'
    __tablename__ = 'admin_role'
    
    admin_id: Mapped[int]  = mapped_column(ForeignKey('admin.id'), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey('role.id'), primary_key=True)


@click.command('create-root-admin')
def create_root_admin():
    """созндыние админа с root ролью, в случае наличия 
    root - происходит замена пароля"""
    with current_app.app_context():
        pass


def init_app(app: Flask):
    app.cli.add_command(create_root_admin)
    