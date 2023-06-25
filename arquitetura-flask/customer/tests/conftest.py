import pytest

from customer.app import create_app, minimal_app
from customer.ext.commands import populate_db
from customer.ext.database import db


@pytest.fixture(scope="session")
def min_app():
    app = minimal_app(FORCE_ENV_FOR_DYNACONF="testing")
    return app


@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        # db.create_all(app=app)
        db.create_all()
        yield app
        # db.drop_all(app=app)
        db.drop_all()


@pytest.fixture(scope="session")
def customers(app):
    with app.app_context():
        return populate_db()
