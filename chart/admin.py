from django.contrib import admin
from django.conf.urls import url

from .views import chart_view
from .models import Book

class ChartAdmin(admin.ModelAdmin):
    readonly_fields = ('charts', )

    def charts(self, obj):
        return '<a href="{}/charts/">Open</a>'.format(obj.pk)
    charts.allow_tags = True

    def get_urls(self):

        urls = super(ChartAdmin, self).get_urls()
        extend_urls = [
            url(r'(?P<object_id>[0-9]+)/charts/$', chart_view),
        ] + urls

        return extend_urls


class BookAdmin(ChartAdmin):
    list_display  = ('id', 'name', 'charts')


admin.site.register(Book, BookAdmin)
