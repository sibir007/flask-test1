from flask.cli import FlaskGroup
import click
from flask import current_app, Flask
from .db import db
from .admin_init import my_admin_datastore
import click
import random
import string
from .admin.model import MyAdmin, Telephone, Role
from .social_gamification.model import User, MarketUser, Tip, Purchase



@click.command('create-root-admin')
def create_root_admin():
    """созндыние админа с root ролью, в случае наличия 
    root - происходит замена пароля"""
    
    with current_app.app_context():
        pass


@click.command('build-test-db')
def build_test_db():
    """создание тестовой базы данных"""
    
    
    with current_app.app_context():
        db.drop_all()
        db.create_all()
        admin_role = my_admin_datastore.create_role(name='admin')
        sg_admin_role = my_admin_datastore.create_role(name='sg_admin')
        root_admin_role = my_admin_datastore.create_role(name='root_admin')
        db.session.add(admin_role)
        db.session.add(sg_admin_role)
        db.session.add(root_admin_role)
        db.session.commit()

        test_root_admin = my_admin_datastore.create_user(
            password='root',
            # name = 'root', password='root',
            email = 'sibiriakoff2006@yandex.ru',
            phones = [Telephone(telephone='88123334455'), Telephone(telephone='89112772308')],
            roles = [admin_role, root_admin_role, sg_admin_role]
        )
        
        names = ['Harry', 'Amelia', 'Oliver', 'Jack']    

        for name in names:
            tmp_email = name.lower() + '_admin@test.com'
            temp_tel1 = ''.join(random.choice(string.digits) for i in range(9)) 
            temp_tel2 = ''.join(random.choice(string.digits) for i in range(9)) 
            temp_pass = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(5)) 
            my_admin_datastore.create_user(
                password=temp_pass,
                # name = name, password=temp_pass,
                email = tmp_email,
                phones = [Telephone(telephone=temp_tel1), Telephone(telephone=temp_tel2)],
                roles = [admin_role,]
            )
        
        db.session.commit()



def init_command(app: Flask):
    app.cli.add_command(create_root_admin)
    app.cli.add_command(build_test_db)
        



