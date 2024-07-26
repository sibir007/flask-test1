from flask_security.core import current_user
from flask_admin.contrib import sqla
from flask import url_for, redirect, request, abort, current_app
from flask_security import login_required
from flask_security.core import Security
from flask_admin import AdminIndexView, expose, Admin


class MyModelsMixin:

    _admin_role_ = None

    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role(self._admin_role_))
    
    def _handle_view(self, name, **kwargs):
        
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))



class MyViewsBase(MyModelsMixin, sqla.ModelView):
    """
    базовый класс для видов всех моделей,
    в субклассах переопределить _admin_role_ из MyModelsMixin 
    """

    column_display_all_relations = True
    create_modal = True
    edit_modal = True
    details_modal = True
    can_view_details = True
    
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
    
# class MyAdminIndexView(AdminIndexView):
#     @expose('/')
#     @login_required
#     def index(self):
#         return self.render('admin/index.html')

# myadmin = Admin(
#     name='CRYPTO MENTORS ADMIN',
#     template_mode='bootstrap4',
#     index_view=MyAdminIndexView()
# )

