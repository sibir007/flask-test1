
import datetime
from typing_extensions import Annotated

from sqlalchemy import func
from sqlalchemy import String

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column



class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

intpk = Annotated[int, mapped_column(primary_key=True)]
timstamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=func.current_timestamp())
]

utc_timstamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=func.UTC_TIMESTAMP())
]
required_name = Annotated[str, mapped_column(String(30), nullable=False)]