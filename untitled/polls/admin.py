from django.contrib import admin
from .models import *
# Register your models here.

class BankAdmin(admin.ModelAdmin):
    list_display = ('idbank', 'address')
    search_fields = ('idbank', 'address')

admin.site.register(BankModel, BankAdmin)

class TranAdmin(admin.ModelAdmin):
    list_display = ('idtran', 'sum', 'type','user','bank','date')
    list_filter = ['sum']
    search_fields = ('id', 'user')

admin.site.register(TransactionModel, TranAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)