from django.contrib import admin
from staff.models import User, Staff
#from django.contrib.auth.admin import UserAdmin
#from .models import Profile

admin.site.register(User)
admin.site.register(Staff)
# admin.site.unregister(group)


# class UserAdmin(UserAdmin):
#   list_display = ('username', 'last_login', 'is_admin', 'is_dr', 'is_rec', 'is_guest')
#  search_fields = ('username', 'email', )
# readonly_fields = ('date_joined', 'last_login',)

#filter_horizontal = ()
#list_filter = ()
#fieldsets = ()
