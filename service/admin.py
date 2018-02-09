from django.contrib import admin
from service.models import *
class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 0


class ServiceAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
    inlines = [ServiceImageInline]

    class Meta:
        model = Service

admin.site.register(Service, ServiceAdmin)


class ServiceImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ServiceImage._meta.fields]

    class Meta:
        model = ServiceImage

admin.site.register(ServiceImage, ServiceImageAdmin)

