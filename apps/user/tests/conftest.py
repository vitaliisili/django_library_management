import pytest

from apps.user.models import User


@pytest.fixture(scope='session')
def raw_password():
    return 'simplePassword'


@pytest.fixture
def admin_user(db, raw_password):
    admin = User.objects.create_user('admin', 'admin@email.com', raw_password)
    return admin


@pytest.fixture
def simple_user(db, raw_password):
    user = User.objects.create_user('simple', 'simple@email.com', raw_password)
    return user


@pytest.fixture
def user_list(admin_user, simple_user):
    return [admin_user, simple_user]
