from django.contrib import admin
from app.models import ProfileModel


class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    list_per_page = 20


admin.site.register(ProfileModel, ProfileModelAdmin)