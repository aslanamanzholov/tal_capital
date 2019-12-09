from django.contrib import admin

from tal_capital.core.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'user',)

    def get_actions(self, request):
        actions = super(PostAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False
