import logging
from .model import Activity
from ..views_base import MyViewsBase
from ..db import db




logger = logging.getLogger('admin.activity.views')


class ABase(MyViewsBase):
    """базвый класс для activity видов"""

    _admin_role_ = 'ac_admin'

class ActivityModelView(ABase):

    column_list = (Activity.tg_id,
                   Activity.year,
                   Activity.week,
                   Activity.messages)

    form_columns = (Activity.tg_id,
                    Activity.year,
                    Activity.week,
                    Activity.messages)

ActivityView = ActivityModelView(Activity, db.session, name='ACTIVITY')