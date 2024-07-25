import datetime
import imp
from typing import List, Optional
from ..db import db
# from flask_sqlalchemy import 
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates, declarative_base
from sqlalchemy import Float, ForeignKey, Text, Uuid, func

# TODO: рассмотреть использование асоциативного объекта
class User(db.Model):

    __tablename__ = 'user'
    __bind_key__ = 'social_gamification'

    # id INTEGER PRIMARY KEY NOT NULL,
    id: Mapped[int] = mapped_column(primary_key=True)
    markets: Mapped[List['MarkerUser']] = relationship(back_populates='market_user.user')
    purchases: Mapped[List['Purchase']] = relationship(back_populates='purchase.user')
    send_tips: Mapped[List['Tip']] = relationship(back_populates='sender_user')
    receiv_tips: Mapped
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




class MarkerUser(db.Model):

    __tablename__ = 'market_user'
    __bind_key__ = 'social_gamification'

    # uid VARCHAR PRIMARY KEY NOT NULL,
    uid: Mapped[Uuid] = mapped_column(primary_key=True)
    # user_id INTEGER,
    # TODO: разобраться может ли быть NULL
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

class Tip(db.Model):

    __tablename__ = 'tip'
    __bind_key__ = 'social_gamification'

    
    # tid INTEGER PRIMARY KEY AUTOINCREMENT,
    tid: Mapped[int] = mapped_column(primary_key=True)
    # sender_id INTEGER NOT NULL,
    sender_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    sender_user: Mapped['User'] = relationship(back_populates='send_tips')
    # receiver_id INTEGER NOT NULL,
    receiver_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    sender_user: Mapped['User'] = relationship(back_populates='receiv_tips')
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
    