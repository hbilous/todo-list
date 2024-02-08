from django.contrib import admin
from todo.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("tags",)
    list_filter = ("is_done",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
