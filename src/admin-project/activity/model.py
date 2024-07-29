import datetime
from typing import List, Optional
from uuid import UUID
from ..db import db
# from flask_sqlalchemy import 
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates, declarative_base
from sqlalchemy import Column, Float, ForeignKey, Integer, Nullable, Text, Uuid, func, Table

class Activity(db.Model):
 
    __tablename__ = 'activity'
    __bind_key__ = 'activity'

    # id INTEGER PRIMARY KEY NOT NULL,
    id: Mapped[int] = mapped_column(primary_key=True)
    # tg_id INTEGER NOT NULL,
    tg_id: Mapped[int]
    # year INTEGER NOT NULL,
    year: Mapped[int]
    # week INTEGER NOT NULL,
    week: Mapped[int]
    # messages INTEGER NOT NULL,
    messages: Mapped[int]
    # created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    created: Mapped[datetime.datetime] = mapped_column(server_default=func.current_timestamp())

