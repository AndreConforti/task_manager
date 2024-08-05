from django.contrib import admin
from .models import Report, SalesManager


class ListingReports(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'subject', 'date_response')
    list_display_links = ('id', 'ticket')
    search_fields = ['subject']
    list_per_page = 25


class ListingSalesManagers(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Report, ListingReports)
admin.site.register(SalesManager, ListingSalesManagers)