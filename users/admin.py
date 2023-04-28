from django.contrib import admin
from .models.users import User
from .models.clients import Client
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass



class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,UserAdmin)

admin.site.register(Client,ClientAdmin)