
from flask_admin.contrib import sqla

from .model import MyAdmin, Role, Telephone
from ..db import db
from flask_admin import BaseView, expose
from ..views_base import MyViewsBase, MyModelsMixin

class AnalyticsView(MyModelsMixin, BaseView):
    """для примера возможного использования"""

    _admin_role_ = 'root_admin'

    @expose('/')
    def index(self):
        return self.render('analytics_index.html')

class MyAdminBase(MyViewsBase):
    """базовый класс для админ видов"""

    _admin_role_ = 'root_admin'
    
    
class MyAdminModelView(MyAdminBase):

    # column_editable_list = ('email', 'phones', 'roles')
    column_list = ('email', 'phones', 'roles')
    form_columns = ('email', 'phones', 'roles')
    # column_details_list = ('email', 'phones', 'roles')
    
    inline_models = (Telephone, )

class RoleModelView(MyAdminBase):
    column_list = ('name', 'description')
    form_columns = ('name', 'description')
    # column_details_list = ('name', 'description')
    
class TelephoneModelView(MyAdminBase):
    column_list = ('telephone', 'admin')
    form_columns = ('telephone', 'admin')
    # column_details_list = ('name', 'description')
    
    
# myadmin.add_view(MyAdminModelView(MyAdmin, db.session, name='admin', category='ADMIN'))
# myadmin.add_view(sqla.ModelView(Telephone, db.session,  name='telephone', category='ADMIN'))
# myadmin.add_view(RoleModelView(Role, db.session, name='role', category='ADMIN'))
# # myadmin.add_view(MyAdminModelView(Role, db.session, category='myadmin'))
# myadmin.add_view(AnalyticsView(name='ANALYTICS', endpoint='analytics'))


MyAdminListView = MyAdminModelView(MyAdmin, db.session, name='admin', category='ADMIN')
MyAdminTelephoneView = TelephoneModelView(Telephone, db.session,  name='telephone', category='ADMIN')
MyAdminRoleView = RoleModelView(Role, db.session, name='role', category='ADMIN')
# myadmin.add_view(MyAdminModelView(Role, db.session, category='myadmin'))
MyAdminAnalyticsView = AnalyticsView(name='ANALYTICS', endpoint='analytics')










    
