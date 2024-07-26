from flask_security import login_required
from flask_admin import AdminIndexView, expose, Admin
from .admin.model import MyAdmin, Role
from flask_security.core import Security
from flask_security.datastore import SQLAlchemyUserDatastore
from .db import db
from flask_admin import helpers as admin_helpers
from flask import url_for



my_admin_datastore = SQLAlchemyUserDatastore(db=db, user_model=MyAdmin, role_model=Role)
security = Security(datastore=my_admin_datastore)
    
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('admin/index.html')

myadmin = Admin(
    name='CRYPTO MENTORS ADMIN',
    template_mode='bootstrap4',
    index_view=MyAdminIndexView()
)


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=myadmin.base_template,
        admin_view=myadmin.index_view,
        h=admin_helpers,
        get_url=url_for
    )


from .admin.views import (
    MyAdminListView, MyAdminTelephoneView,
    MyAdminRoleView, MyAdminAnalyticsView
    )
from .social_gamification.views import (
    SGUserView, SGMarketUserView,
    SGPurchaseView, SGTipView
)

myadmin.add_views(
    MyAdminListView, MyAdminTelephoneView,
    MyAdminRoleView, MyAdminAnalyticsView,
    SGUserView, SGMarketUserView,
    SGPurchaseView, SGTipView
)