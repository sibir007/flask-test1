from .model import User, MarketUser, Purchase, Tip
from flask_admin import BaseView
from flask_admin.contrib import sqla
# from flask import Flask, url_for, redirect, request, abort, current_app
from ..views_base import MyViewsBase
from ..db import db

class SGBase(MyViewsBase):
    """базвый класс для social_gamification видов"""

    _admin_role_ = 'sg_admin'

class SGUserModelView(SGBase):
    # TODO: определиться с составом columns social_gamification.user list view 
    column_list = ('tg_nickname', 
                   'tg_status', 
                   'chat_name',
                   'status',
                   'whitelist',
                   'ban',
                   'markets',
                   'purchases',
                #    'receiv_tips'
                #    'send_tip',
                   )
    # TODO: определиться с составом columns social_gamification.user form 
    form_columns = ('tg_nickname', 
                   'tg_status', 
                   'chat_name',
                   'status',
                   'whitelist',
                   'ban',
                   'markets',
                   'purchases',
                #    'send_tip',
                #    'receiv_tips'
                   )
    # TODO: определиться с составом columns social_gamification.user details view 
    # column_details_list = ('tg_nickname', 
    #                'tg_status', 
    #                'chat_name',
    #                'status',
    #                'whitelist',
    #                'ban',
    #                'markets',
    #                'purchases',
    #                'send_tip',
    #                'receiv_tips')
    
    inline_models = (MarketUser, Purchase)
    # inline_models = (MarketUser, Purchase, Tip)
    
class SGMarketUserModelView(SGBase):
    
    column_list = ('user',
                   'trading_amount',
                   'spot_trading',
                   'futures_trading',
                   'assets')
    
    form_columns = ('user',
                   'trading_amount',
                   'spot_trading',
                   'futures_trading',
                   'assets')

    # column_details_list = ('user',
    #                'trading_amount',
    #                'spot_trading',
    #                'futures_trading',
    #                'assets')
    
class SGPurchaseModelView(SGBase):
    
    column_list = ('user',
                   'amount',
                   'total_price',
                   'user_balance')
    
    form_columns = ('user',
                   'amount',
                   'total_price',
                   'user_balance')
    
    # column_details_list = ('user',
    #                     'amount',
    #                     'total_price',
    #                     'user_balance')
    
    
class SGTipModelView(SGBase):
    
    column_list = (
                #     Tip.sender_user,
                #    Tip.receiver_user,
                   Tip.amount,
                   Tip.receiver_tips_amount,
                   Tip.sender_cmpoints_amount,
                   Tip.sender_tips_amount,
                   Tip.receiver_cmpoints_amount)

    form_columns = (
                #     Tip.sender_user,
                #    Tip.receiver_user,
                   Tip.amount,
                   Tip.receiver_tips_amount,
                   Tip.sender_cmpoints_amount,
                   Tip.sender_tips_amount,
                   Tip.receiver_cmpoints_amount)
    
    # column_details_list = (Tip.sender_user,
    #                Tip.receiver_user,
    #                Tip.amount,
    #                Tip.receiver_tips_amount,
    #                Tip.sender_cmpoints_amount,
    #                Tip.sender_tips_amount,
    #                Tip.receiver_cmpoints_amount)
    
# myadmin.add_view(SGUserModelView(User, db.session, name='user', category='SG'))
# myadmin.add_view(SGMarketUserModelView(MarketUser, db.session, name='market_user', category='SG'))
# myadmin.add_view(SGPurchaseModelView(Purchase, db.session, name='purchase', category='SG'))
# # myadmin.add_view(SGTipModelView(Tip, db.session, name='tip', category='SG'))
SGUserView = SGUserModelView(User, db.session, name='user', category='SG')
SGMarketUserView = SGMarketUserModelView(MarketUser, db.session, name='market_user', category='SG')
SGPurchaseView = SGPurchaseModelView(Purchase, db.session, name='purchase', category='SG')
SGTipView = SGTipModelView(Tip, db.session, name='tip', category='SG')




    