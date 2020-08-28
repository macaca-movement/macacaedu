from django.contrib import admin

from study.models import Activity, ActivityItem, StudyMedia


@admin.register(StudyMedia)
class StudyMediaAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ["name"]


@admin.register(ActivityItem)
class ActivityItemAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ["name"]
    autocomplete_fields = ["medias"]


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ["name"]
    autocomplete_fields = ["items"]
