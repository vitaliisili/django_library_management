from django.db import models
from django.contrib.auth import models as authmodel
class User(authmodel.User):
    pass
