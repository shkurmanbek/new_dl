from django.contrib import admin

# Register your models here.
from research.models import Research

class ResearchAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'pdf', 'cover']

admin.site.register(Research, ResearchAdmin)
