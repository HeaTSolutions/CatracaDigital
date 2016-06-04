from django.contrib import admin
from .models import Plan


class PlanModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'monthly_price', 'users', 'automatic_register', 'dynamic_reminders',
                    'support_all_time', 'is_popular', 'is_free', 'created_at', 'modified_at')


admin.site.register(Plan, PlanModelAdmin)
