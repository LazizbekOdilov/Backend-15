from django.contrib import admin

from .models import *

@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    search_fields = ["ism"]

@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_display = ["nom", "aktiv"]
    search_fields = ["nom"]
    list_filter = ["aktiv"]


@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ["nom", "yonalish", "asosiy"]
    list_filter = ["asosiy", "yonalish"]
    search_fields = ["nom"]

# admin.site.register(Yonalish)
# admin.site.register(Fan)
# admin.site.register(Ustoz)