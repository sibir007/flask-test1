import os
import tempfile

from flask import Flask
import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

sql_data_fiel = os.path.join(os.path.dirname(__file__), 'data.sql')
with open(sql_data_fiel, 'rb') as f:
    _data_sql = f.read().decode('utf-8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path
    })
    
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)
    
    yield app
    
    os.close(db_fd)
    os.unlink(db_path)
    
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app: Flask):
    return app.test_cli_runner()