from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import useraccount

# Register your models here.
class AccountAdmin(UserAdmin):
    ordering = ("email",)
    list_display = ("first_name","last_name","email","phone_number","date_joined","last_login")
    search_fields = ("email","phone_number")
    readonly_fields = ("date_joined","last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(useraccount,AccountAdmin)