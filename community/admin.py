from django.contrib import admin
from community.models import Community

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

# Register your models here.
