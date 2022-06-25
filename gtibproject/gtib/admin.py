from django.contrib import admin, messages
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from gtib.models import PageSettings, SocialMediaAccount, NewsTypeModel, NewsCategoryModel, NewsModel, FAQsModel, FormmModel, FormmChoices, OfferQuestionModel, VolunteersModel, EventModel

class SocialMediaAccountAdmin(admin.TabularInline):
    model = SocialMediaAccount
    extra = 1

@admin.register(PageSettings)
class PageSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("ƏSAS SƏHİFƏ META MƏLUMATLARI"), {'fields': ('logo', 'footer_logo', 'headerbgimg', 'favicon', 'title', 'description', 'keywords')}),
        (_("ƏLAQƏ MƏLUMATLARI"), {'fields': ('phone_number', 'email', 'address', 'footer_map', 'footer_map_link')}),
        (_("DİGƏR MƏLUMATLAR"), {'fields': ('about', 'charter')}),
    )
    inlines = [SocialMediaAccountAdmin]

    def save_model(self, request, obj, form, change):
        super(PageSettingsAdmin, self).save_model(request, obj, form, change)
        if obj != PageSettings.objects.first():
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Birdən çox parametrlər modeli əlavə edilə bilməz!")

class FormmChoicesAdmin(admin.TabularInline):
    model = FormmChoices
    extra = 3

@admin.register(FormmModel)
class FormmAdmin(admin.ModelAdmin):
    inlines = [FormmChoicesAdmin]

admin.site.register(NewsTypeModel)
admin.site.register(NewsCategoryModel)
admin.site.register(NewsModel)
admin.site.register(FAQsModel)
admin.site.register(OfferQuestionModel)
admin.site.register(VolunteersModel)
admin.site.register(EventModel)


AdminSite.site_title = _("Djangoo site admin")
AdminSite.site_header = _("Djangoo administration")
AdminSite.index_title = _("Sitee administration")