from django.contrib import admin


from .models import TodoList

@admin.register(TodoList)
class TodoBoardAdmin(admin.ModelAdmin):
    list_display = (
        'no',
        'pcode',
        'user_id',
        'title',
        'content',
        'is_complete',
        'priority',
        'end_date',
    )
