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
    index_view=MyAdminIndexView(),
    base_template='admin/master.html'
)





@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=myadmin.base_template,
        admin_view=myadmin.index_view,
        h=admin_helpers,
        get_url=url_for
    )
    
    
from flask_security.proxies import _security
from flask_security.decorators import unauth_csrf, auth_required, roles_accepted
from flask_security.forms import build_form_from_request
from flask_security.utils import view_commit
from flask_security.registerable import register_user
from flask.ctx import after_this_request
from flask.typing import ResponseValue
from flask_admin.contrib import sqla
from flask import Blueprint, redirect, render_template, request


register_bp = Blueprint('register', __name__, url_prefix='/admin')

# ПЕРЕОБРЕДЕЛИНЕ РЕГИСТРАЦИИ Flask-Security !!!!!!!!!
@register_bp.route('/register', methods=['GET', 'POST'])
@unauth_csrf()
@auth_required()
@roles_accepted('root_admin')
def register() -> ResponseValue:
    form_name = "register_form"
    form = build_form_from_request(form_name)

    if form.validate_on_submit():
        after_this_request(view_commit)
        register_user(form)

        return redirect('/admin/myadmin')

    return render_template('security/register_user.html', 
                           register_user_form=form, 
                           admin_base_template=myadmin.base_template,
                            admin_view=myadmin.index_view,
                            h=admin_helpers,
                            get_url=url_for)
    






from .admin.views import (
    MyAdminListView, # MyAdminTelephoneView,
    MyAdminRoleView, MyAdminAnalyticsView
    )
from .social_gamification.views import (
    SGUserView, SGMarketUserView,
    SGPurchaseView, SGTipView
)

from .activity.views import (
    ActivityView
)

myadmin.add_views(
    MyAdminListView, # MyAdminTelephoneView,
    MyAdminRoleView, MyAdminAnalyticsView,
    SGUserView, SGMarketUserView,
    SGPurchaseView, SGTipView,
    ActivityView
)