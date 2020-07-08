from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """ List Admin Definition """

    list_display = (
        "name",
        "user",
        "count_rooms",
    )

    search_fields = ("name",)
    # ^ startswith 시작 문자

    filter_horizontal = ("rooms",)
