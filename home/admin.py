from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'due_date', 'completed']

admin.site.register(Task, TaskAdmin)
