from django.contrib import admin

# Register your models here.
from app.models import Skill, Blog, Contact

admin.site.register(Skill)
admin.site.register(Blog)
admin.site.register(Contact)