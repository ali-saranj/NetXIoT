from django.contrib import admin

from home.models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'email', 'phone', 'interests', 'create_at', 'status')
    list_filter = ('create_at', 'status')
    search_fields = ('name', 'email', 'phone', 'pk', 'status')
    ordering = ('-create_at',)
