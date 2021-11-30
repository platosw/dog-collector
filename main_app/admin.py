from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Dog, Toy, Feeding, Photo, Owner

class OwnerInline(admin.StackedInline):
    model = Owner
    can_delete = False
    verbose_name_plurel = 'owner'

# define a new user admin
class UserAdmin(BaseUserAdmin):
    inlines = (OwnerInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(Dog)
admin.site.register(Toy)
admin.site.register(Feeding)
admin.site.register(Photo)
