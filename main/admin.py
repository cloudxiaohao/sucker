from django.contrib import admin
from models import *

# Register your models here.
class AdminLogin(admin.ModelAdmin):
	list_display = ['lname','lpassword','lemail']

admin.site.register(Login)
admin.site.register(UserInfo)
admin.site.register(AddressInfo)
admin.site.register(OrderInfo)
admin.site.register(CartInfo)
admin.site.register(GoodInfo)
admin.site.register(Comment)
admin.site.register(ViewInfo)
admin.site.register(Dict)
admin.site.register(Log)