from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mover.models import Mover

admin.site.register(Mover, UserAdmin)
