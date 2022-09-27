from django.contrib import admin
from weatherapp.models import SearchedCity
# Register your models here.
class SearchedCityAdmin(admin.ModelAdmin):
    list_display=('city', 'temperature', 'sent_at', 'updated', 'image')
    search_fields=['city']
    list_filter=('sent_at', 'updated')
    list_editable=['temperature']
    readonly_fields=['city', 'sent_at', 'updated']
admin.site.register(SearchedCity, SearchedCityAdmin)

