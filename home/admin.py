from django.contrib import admin
from home.models import*
class ServiceImageInline(admin.TabularInline):
    model = HomeImage
    extra = 0

class HomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Home._meta.fields]
    inlines = [ServiceImageInline]

    class Meta:
        model = Home

admin.site.register(Home, HomeAdmin)

class HomeImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in HomeImage._meta.fields]

    class Meta:
        model = HomeImage

admin.site.register(HomeImage, HomeImageAdmin)