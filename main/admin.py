from django.contrib import admin
from django.contrib.auth.models import User

from main.models import *

admin.site.register(Categoriya)
admin.site.register(Productos)
admin.site.register(UserProfile)
