from django.contrib import admin
from .models import*
#
# class AboutlInline(admin.StackedInline):
#    model = ShortAbout
#    extra = 1

class FaqAdmin(admin.ModelAdmin):
    fields = [
        'faq_title',
        'faq_text',
        # 'about_image',

    ]
    list_display = ('faq_title','faq_text')
    inlines = [
        # AboutlInline
    ]
admin.site.register(Faq, FaqAdmin)

