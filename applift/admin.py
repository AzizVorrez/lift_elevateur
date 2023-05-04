from django.contrib import admin
from .models import Communes, Cities, Keywords

admin.site.register(Keywords)

class CitiesInline(admin.StackedInline):
    model = Cities
    extra = 1

class CommunesAdmin(admin.ModelAdmin):
    inlines = [CitiesInline]

admin.site.register(Communes, CommunesAdmin)
