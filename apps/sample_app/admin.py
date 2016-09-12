from django.contrib import admin
from apps.sample_app.models import SampleModel


class SampleModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(SampleModel, SampleModelAdmin)
