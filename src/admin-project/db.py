
import datetime
from typing import Mapping
from typing_extensions import Annotated
from flask import Flask, current_app
from sqlalchemy import func
from sqlalchemy import String, MetaData, Table
import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

# from flaskr.db import init_app

intpk = Annotated[int, mapped_column(primary_key=True)]
timstamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=func.current_timestamp(), init=False)
]

utc_timstamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=func.UTC_TIMESTAMP())
]
required_name = Annotated[str, mapped_column(String(30), nullable=False)]

    
 
# DefaultBase.metadata.create_all(some_engine)
# OtherBase.metadata.create_all(some_other_engine)


class MyMixin:
    @classmethod
    def __table_cls__(cls, name, metadata_obj, *arg, **kw):
        return Table(f"my_{name}", metadata_obj, *arg, **kw)
  
# The above mixin would cause all Table objects generated to 
# include the prefix "my_", followed by the name normally 
# specified using the __tablename__ attribute.

class PkMixin:
    id: Mapped[intpk]

class CereatedAtUTCMixin:
    created_at: Mapped[utc_timstamp]    

class CereatedAtMixin:
    created_at: Mapped[timstamp]    


class PkCereatedAtUTCMixin(PkMixin, CereatedAtUTCMixin):
    pass

class PkCereatedAtMixin(PkMixin, CereatedAtMixin):
    pass



class Base(DeclarativeBase):
    pass



db = SQLAlchemy(model_class=Base)


