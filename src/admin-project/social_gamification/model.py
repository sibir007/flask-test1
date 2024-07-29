import datetime
from typing import List, Optional
from uuid import UUID
from ..db import db
# from flask_sqlalchemy import 
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates, declarative_base
from sqlalchemy import Column, Float, ForeignKey, Integer, Nullable, Text, Uuid, func, Table


# tip_table = Table(
#     'tip',
#     db.Model.metadata,
#     Column('tid', Integer, primary_key=True),
#     Column('sender_id', Integer, ForeignKey('user.id')),
#     Column('receiver_id', Integer, ForeignKey('user.id')),
#     Column('amount', Integer),
#     Column('receiver_tips_amount', Integer),
#     Column('sender_cmpoints_amount', Integer),
#     Column('sender_tips_amount', Integer),
#     Column('receiver_cmpoints_amount', Integer),
#     Column('created', Integer),
#     __bind_key__ = 'social_gamification'
# )    
class Tip(db.Model):

    __tablename__ = 'tip'
    __bind_key__ = 'social_gamification'

    
    # tid INTEGER PRIMARY KEY AUTOINCREMENT,
    tid: Mapped[int] = mapped_column(primary_key=True)
    # sender_id INTEGER NOT NULL,
    sender_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    sender_user: Mapped['User'] = relationship(foreign_keys=[sender_id])
    # receiver_id INTEGER NOT NULL,
    receiver_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    receiver_user: Mapped['User'] = relationship(foreign_keys=[receiver_id])
    # receiver_user: Mapped['User'] = relationship(back_populates='receiv_tips')
    # amount INTEGER NOT NULL,
    amount: Mapped[int]
    # receiver_tips_amount INTEGER NOT NULL,
    receiver_tips_amount: Mapped[int]
    # sender_cmpoints_amount INTEGER NOT NULL,
    sender_cmpoints_amount: Mapped[int]
    # sender_tips_amount INTEGER NOT NULL,
    sender_tips_amount: Mapped[int]
    # receiver_cmpoints_amount INTEGER NOT NULL,
    receiver_cmpoints_amount: Mapped[int]
    # created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created: Mapped[datetime.datetime] = mapped_column(server_default=func.current_timestamp())
    # FOREIGN KEY (sender_id) REFERENCES user (id),
    # FOREIGN KEY (receiver_id) REFERENCES user (id)


# TODO: рассмотреть использование асоциативного объекта
class User(db.Model):

    __tablename__ = 'user'
    __bind_key__ = 'social_gamification'

    # id INTEGER PRIMARY KEY NOT NULL,
    id: Mapped[int] = mapped_column(primary_key=True)
    markets: Mapped[List['MarketUser']] = relationship(back_populates='user')
    purchases: Mapped[List['Purchase']] = relationship(back_populates='user')
    # send_tips: Mapped[List['User']] = relationship(
    #     back_populates='receiv_tips',
    #     primaryjoin= id == tip_table.c.sender_id,
    #     secondaryjoin= id == tip_table.c.receiver_id,
    #     secondary=tip_table)
    # receiv_tips: Mapped[List['User']] = relationship(
    #     back_populates='send_tips',
    #     primaryjoin= id == tip_table.c.receiver_id,
    #     secondaryjoin= id == tip_table.c.sender_id,
    #     secondary=tip_table)
    # send_tips: Mapped[List['Tip']] = relationship(foreign_keys=[Tip.sender_id])
    # receiv_tips: Mapped[List['User']] = relationship(foreign_keys=[Tip.receiver_id])
    # tg_nickname TEXT  NOT NULL,
    tg_nickname: Mapped[str]
    # tg_status TEXT  NOT NULL,
    tg_status: Mapped[str]
    # chat_name TEXT  NOT NULL,
    chat_name: Mapped[str]
    # status TEXT  NOT NULL,
    status: Mapped[str]
    # whitelist BOOLEAN NOT NULL,
    whitelist: Mapped[bool]
    # ban BOOLEAN NOT NULL,
    ban: Mapped[bool]
    # cm_points_per_month INTEGER NOT NULL,
    cm_points_per_month: Mapped[int]
    # cm_points INTEGER NOT NULL,
    cm_points: Mapped[int]
    # class TEXT NOT NULL,
    class_: Mapped[str] = mapped_column(name='class')
    # tips INTEGER NOT NULL,
    tips: Mapped[int]
    # tips_amount INTEGER NOT NULL,
    tips_amount: Mapped[int]
    # activity INTEGER NOT NULL,
    activity: Mapped[int]
    # multiplier FLOAT(16) NOT NULL,
    multiplier = mapped_column(Float(16))
    # total_earned_cm INTEGER NOT NULL,
    total_earned_cm: Mapped[int]
    # signal_access BOOLEAN NOT NULL,
    signal_access: Mapped[bool]
    # created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    created: Mapped[datetime.datetime] = mapped_column(server_default=func.current_timestamp())

    # TODO: определиться с репрезентацией юзера
    def __str__(self) -> str:
        return f"tg_nickname={self.tg_nickname}, chat_name={self.chat_name}"

# TODO: из sql не понятно отношение social_gamification.user к market_user: many-to-one | one-to-one 
class MarketUser(db.Model):

    __tablename__ = 'market_user'
    __bind_key__ = 'social_gamification'

    # uid VARCHAR PRIMARY KEY NOT NULL,
    uid: Mapped[UUID] = mapped_column(primary_key=True)
    # user_id INTEGER,
    # TODO: является ли social_gamification.market_user.user_id nullable
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='markets')
    # trading_amount FLOAT(16) NOT NULL,
    trading_amount = mapped_column(Float(16), nullable=False)
    # spot_trading FLOAT(16) NOT NULL,
    spot_trading = mapped_column(Float(16), nullable=False)
    # futures_trading FLOAT(16) NOT NULL,
    futures_trading = mapped_column(Float(16), nullable=False)
    # assets FLOAT(16) NOT NULL,
    assets = mapped_column(Float(16), nullable=False)
    # created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created: Mapped[datetime.datetime] = mapped_column(server_default=func.current_timestamp())
    # FOREIGN KEY (user_id) REFERENCES user (id)

    # TODO: разобраться с репрезентацией social_gamification.market_user  
    def __str__(self) -> str:
        return f"trading_amount={self.trading_amount}, futures_trading={self.futures_trading}, spot_trading={self.spot_trading}, assets={self.assets}"

class Purchase(db.Model):
    
    __tablename__ = 'purchase'
    __bind_key__ = 'social_gamification'

    
    # pid INTEGER PRIMARY KEY AUTOINCREMENT,
    pid: Mapped[int] = mapped_column(primary_key=True)
    # user_id INTEGER NOT NULL,
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='purchases')
    # amount INTEGER NOT NULL,
    amount: Mapped[int]
    # total_price FLOAT(8) NOT NULL,
    total_price = mapped_column(Float(8), nullable=False)
    # user_balance FLOAT(8) NOT NULL,
    user_balance = mapped_column(Float(8), nullable=False)
    # created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created: Mapped[datetime.datetime] = mapped_column(server_default=func.current_timestamp())
    # FOREIGN KEY (user_id) REFERENCES user (id)

