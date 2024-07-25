from flask_security.datastore import SQLAlchemyUserDatastore
from flask import (
    Flask, url_for, redirect, 
    render_template, request, 
    abort, current_app
    )
import flask_admin
from flask_admin.contrib import sqla
from ..db import db
from .model import MyAdmin, Role, Telephone
from flask_security.core import Security, current_user
from flask_security import login_required
from flask_admin import helpers as admin_helpers
import click
from flask import Flask, current_app
import random
import string
from flask_admin import BaseView, expose, AdminIndexView


my_admin_datastore = SQLAlchemyUserDatastore(db=db, user_model=MyAdmin, role_model=Role)
security = Security(datastore=my_admin_datastore)


class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('analytics_index.html')

class MyAdminModelView(sqla.ModelView):
    # column_editable_list = ('email', 'phones', 'roles')
    column_list = ('email', 'phones', 'roles')
    form_columns = ('email', 'phones', 'roles')
    details_list = ('email', 'phones', 'roles')
    
    column_display_all_relations = True
    create_modal = True
    edit_modal = True
    can_view_details = True
    inline_models = (Telephone, )
    
    # column_hide_backref = 
    # column_searchable_list = ['name', 'email']
    # column_filters = ['country']
    # column_editable_list = ['name', 'last_name']
    # form_choices = {
    #     'title': [
    #         ('MR', 'Mr'),
    #         ('MRS', 'Mrs'),
    #         ('MS', 'Ms'),
    #         ('DR', 'Dr'),
    #         ('PROF', 'Prof.')
    #     ]
    # }
    # form_excluded_columns = ['last_name', 'email']
    # can_export = True
    
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('root_admin'))
    
    def _handle_view(self, name, **kwargs):
        
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

class RoleModelView(sqla.ModelView):
    column_list = ('name', 'description')
    form_columns = ('name', 'description')
    details_list = ('name', 'description')
    
    create_modal = True
    edit_modal = True
    
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('admin/index.html')

myadmin = flask_admin.Admin(
    name='CRYPTO MENTORS ADMIN',
    template_mode='bootstrap4',
    index_view=MyAdminIndexView()
)



myadmin.add_view(MyAdminModelView(MyAdmin, db.session, name='admin', category='ADMIN'))
myadmin.add_view(sqla.ModelView(Telephone, db.session,  name='telephone', category='ADMIN'))
myadmin.add_view(RoleModelView(Role, db.session, name='role', category='ADMIN'))
# myadmin.add_view(MyAdminModelView(Role, db.session, category='myadmin'))
myadmin.add_view(AnalyticsView(name='ANALYTICS', endpoint='analytics'))


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=myadmin.base_template,
        admin_view=myadmin.index_view,
        h=admin_helpers,
        get_url=url_for
    )
    
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
        root_admin_role = my_admin_datastore.create_role(name='root_admin')
        db.session.add(admin_role)
        db.session.add(root_admin_role)
        db.session.commit()

        test_root_admin = my_admin_datastore.create_user(
            password='root',
            # name = 'root', password='root',
            email = 'sibiriakoff2006@yandex.ru',
            phones = [Telephone(telephone='88123334455'), Telephone(telephone='89112772308')],
            roles = [admin_role, root_admin_role]
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
        



