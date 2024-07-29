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


class MyAdmin(PkCereatedAtMixin, UserMixin, db.Model):
    
    # __bind_key__ = 'admin'

    password: Mapped[str]
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
    # @validates('password')                                                 
    # def hashing_password(self, key, password):
    #     return hash_password(password)
    # status: Mapped[Status]
    # status: Mapped[Status] = mapped_column(
    #     sqlalchemy.Enum("pending", "received", "completed", name="status_enum")
    # )
    
    def __repr__(self) -> str:
        return f"MyAdmin(id={self.id}, email={self.email})"
    
    def __str__(self) -> str:
        return self.email
    
    
class Telephone(PkMixin, db.Model):
    
    # __bind_key__ = 'admin'
    
    telephone: Mapped[str]
    my_admin_id: Mapped[int] = mapped_column(ForeignKey('my_admin.id'))
    admin: Mapped['MyAdmin'] = relationship(back_populates='phones')
    
    def __repr__(self) -> str:
        return f"Telephone(id={self.id!r}, telephone={self.telephone!r})"
    
    def __str__(self) -> str:
        return self.telephone

    
class Role(PkMixin, RoleMixin, db.Model):
    """таблица раолей админов для организации доступа
    к администрируемым сущьностям"""
    # __bind_key__ = 'admin'

    __tablename__ = 'role'
    
    name: Mapped[required_name]
    description: Mapped[Optional[str]]
    my_admins: Mapped[Optional[List['MyAdmin']]] = relationship(
        secondary='admin_role', back_populates='roles'
    )
    
    def __repr__(self) -> required_name:
        return f"Role(name={self.name}, description={self.description})"

    def __str__(self) -> str:
        return self.name

    
admin_role = db.Table(
    'admin_role',
    db.Model.metadata,
    Column('role_id', ForeignKey('role.id'), primary_key=True),
    Column('my_admin_id', ForeignKey('my_admin.id'), primary_key=True),
    # __bind_key__ = 'admin'
)



    