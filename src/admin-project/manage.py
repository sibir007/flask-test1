from flask.cli import FlaskGroup
from faker import Faker
import click
from flask import current_app, Flask
from flask_security import hash_password
from .activity.model import Activity
from .db import db
from .admin_init import my_admin_datastore
import click
import random
import string
from .admin.model import MyAdmin, Telephone, Role
from .social_gamification.model import User, MarketUser, Tip, Purchase
import random


face = Faker()


@click.command('create-root-admin')
def create_root_admin():
    """созндыние админа с root ролью, в случае наличия 
    root - происходит замена пароля"""
    
    with current_app.app_context():
        pass


# @click.command('build-test-admin-db')
def build_test_admin_db():
    """создание тестовой базы данных admin"""
    
    with current_app.app_context():
        db.drop_all(bind_key=None)
        db.create_all(bind_key=None)
        ac_admin_role = my_admin_datastore.create_role(name='ac_admin')
        sg_admin_role = my_admin_datastore.create_role(name='sg_admin')
        root_admin_role = my_admin_datastore.create_role(name='root_admin')
        db.session.add(ac_admin_role)
        db.session.add(sg_admin_role)
        db.session.add(root_admin_role)
        db.session.commit()

        test_root_admin = my_admin_datastore.create_user(
            password = hash_password('root'),
            # name = 'root', password='root',
            email = 'sibiriakoff2006@yandex.ru',
            phones = [Telephone(telephone='88123334455'), Telephone(telephone='89112772308')],
            roles = [ac_admin_role, root_admin_role, sg_admin_role]
        )
        
        names = ['Harry', 'Amelia', 'Oliver', 'Jack']    
        # passw = ['Harrypass', 'Ameliapass', 'Oliverpass', 'Jackpass']
        for name in names:
            tmp_email = name.lower() + '_admin@test.com'
            temp_tel1 = ''.join(random.choice(string.digits) for i in range(9)) 
            temp_tel2 = ''.join(random.choice(string.digits) for i in range(9)) 
            temp_pass = hash_password(name + 'passw')
            my_admin_datastore.create_user(
                password=temp_pass,
                # name = name, password=temp_pass,
                email = tmp_email,
                phones = [Telephone(telephone=temp_tel1), Telephone(telephone=temp_tel2)],
                roles = [ac_admin_role,]
            )
        
        db.session.commit()

# @click.command('build-test-sg-db')
def build_test_sg_db():
    """создание тестовой базы данных social_gamification"""
    
    with current_app.app_context():
        db.drop_all(bind_key='social_gamification')
        db.create_all(bind_key='social_gamification')
        tg_nicknames = [face.unique.user_name() for i in range(20)]
        chat_names = [face.unique.user_name() for i in range(20)]
        tg_statuses = [face.unique.pystr(min_chars=4,max_chars=6) for i in range(10)]
        statuses = [face.unique.pystr(min_chars=4,max_chars=6) for i in range(10)]
        for tn, cn in list(zip(tg_nicknames, chat_names)):
            user = User()
            user.tg_nickname = tn
            # tg_status TEXT  NOT NULL,
            user.tg_status = random.choice(tg_statuses)
            # chat_name TEXT  NOT NULL,
            user.chat_name = cn
            # status TEXT  NOT NULL,
            user.status = random.choice(statuses)
            # whitelist BOOLEAN NOT NULL,
            user.whitelist = face.boolean()
            # ban BOOLEAN NOT NULL,
            user.ban = face.boolean()
            # cm_points_per_month INTEGER NOT NULL,
            user.cm_points_per_month = face.pyint()
            # cm_points INTEGER NOT NULL,
            user.cm_points = face.pyint()
            # class TEXT NOT NULL,
            user.class_ = face.pyint()
            # tips INTEGER NOT NULL,
            user.tips = face.pyint()
            # tips_amount INTEGER NOT NULL,
            user.tips_amount = face.pyint()
            # activity INTEGER NOT NULL,
            user.activity = face.pyint()
            # multiplier FLOAT(16) NOT NULL,
            user.multiplier =  face.pyfloat(right_digits=3)
            # total_earned_cm INTEGER NOT NULL,
            user.total_earned_cm = face.pyint()
            # signal_access BOOLEAN NOT NULL,
            user.signal_access = face.boolean()

            db.session.add(user)

        db.session.commit()

# @click.command('build-test-ac-db')
def build_test_ac_db():
    """создание тестовой базы данных Activity"""
    face = Faker()
    
    with current_app.app_context():
        db.drop_all(bind_key='activity')
        db.create_all(bind_key='activity')
    
        for _ in range(100):
            ac = Activity()
            # tg_id INTEGER NOT NULL,
            ac.tg_id = face.unique.pyint(max_value=1_000_000)
            # year INTEGER NOT NULL,
            ac.year = face.pyint(min_value=2015, max_value=2024)
            # week INTEGER NOT NULL,
            ac.week = face.pyint(min_value=1, max_value=48)
            # messages INTEGER NOT NULL,
            ac.messages = face.pyint(max_value=340)
    
            db.session.add(ac)

        db.session.commit()


@click.command('build-test-admin-sg-ac-db')
def build_test_admin_sg_ac_db():
    build_test_admin_db()
    build_test_sg_db()
    build_test_ac_db()



def init_command(app: Flask):
    # app.cli.add_command(build_test_sg_db)
    # app.cli.add_command(build_test_admin_db)
    # app.cli.add_command(build_test_ac_db)
    app.cli.add_command(build_test_admin_sg_ac_db)
        



