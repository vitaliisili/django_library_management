from django.urls import reverse
from apps.user.forms import SigninForm, SignupForm
from apps.user.models import User


def test_signin_form_is_valid(admin_user, raw_password):
    form = SigninForm(data={"username": admin_user.username, "password": raw_password})
    assert form.is_valid()


def test_signin_form_is_valid_error_password(admin_user):
    form = SigninForm(data={"username": admin_user.username, "password": 'wrong'})
    assert not form.is_valid()


def test_signin_form_is_valid_error_username(admin_user, raw_password):
    form = SigninForm(data={"username": 'wrong_username', "password": raw_password})
    assert not form.is_valid()


def test_login_user_success(admin_user, client):
    client.force_login(admin_user)
    response = client.get(reverse('dashboard'))
    assert response.status_code == 200


def test_login_user_with_wrong_username(admin_user, client, raw_password):
    response = client.login(username='wrong_username', password=raw_password)
    assert not response


def test_login_user_with_wrong_password(admin_user, client):
    response = client.login(username=admin_user.username, password='wrong_password')
    assert not response


def test_registration_form_success(db, raw_password):
    data = {
        'username': 'new_user',
        'email': 'test@email.com',
        'password1': raw_password,
        'password2': raw_password
    }
    form = SignupForm(data=data)
    assert form.is_valid()


def test_registration_user_success(db, client, raw_password):
    data = {
        'username': 'new_user',
        'email': 'test@email.com',
        'password1': raw_password,
        'password2': raw_password
    }

    response = client.post(reverse('sign-up'), data)

    assert response.status_code == 302
    assert User.objects.filter(username=data['username']).exists()
