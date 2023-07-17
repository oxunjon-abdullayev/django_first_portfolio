from django.contrib import admin

# Register your models here.
from app.models import Skill, Blog, Contact


class BlogAdmin(admin.ModelAdmin):
    list_diplay = ['image', 'title', 'description', 'user']


class SkillAdmin(admin.ModelAdmin):
    list_diplay = ['title', 'description']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Contact)


