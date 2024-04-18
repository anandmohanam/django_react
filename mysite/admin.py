from django.contrib import admin
from mysite.models import Person

# Register your models here.

class table_data(admin.ModelAdmin):
    list_display = ('name', 'place', 'age')

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True
    
admin.site.register(Person,table_data)