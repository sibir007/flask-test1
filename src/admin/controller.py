from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound



admin_blueprint = Blueprint('admin', 
                          __name__, 
                          static_folder='static/admin',
                          template_folder='templates/admin')


@admin_blueprint.route('/login')
def login():
    pass

@admin_blueprint.route('/logout')
def logout():
    pass

@admin_blueprint.route('/admin')
def ():
    pass

@admin_blueprint.route('/admin/admins')
def


# admin_blueprint = Blueprint('admin', 
#                             __name__, 
#                             template_folder='templates')
# @admin_blueprint.route('/', defaults={'page': 'index'})
# @admin_blueprint.route('/<page>')
# def show(page):
#     try:
#         return render_template(f'pages/{page}.html')
#     except TemplateNotFound:
#         abort(404)

# @admin_blueprint.errorhandler(404)
# def page_not_found(e):
#     return render_template('pages/404.html')