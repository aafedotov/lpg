from django.contrib import admin

from .models import Task, Category


class TaskAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'author', 'category', 'pub_date',)
    list_editable = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
