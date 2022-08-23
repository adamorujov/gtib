from django.contrib import admin, messages
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from gtib.models import (PageSettings, SocialMediaAccount, NewsTypeModel, 
                        NewsCategoryModel, NewsModel, FAQsModel, 
                        FormmModel, FormmChoices, OfferQuestionModel, 
                        VolunteersModel, EventModel, VolunteerModel, 
                        DirectorModel, PartnerModel,EBookModel, 
                        OfferModel, IdeaModel, PhotoModel, PhotosModel)

class SocialMediaAccountAdmin(admin.TabularInline):
    model = SocialMediaAccount
    extra = 1

@admin.register(PageSettings)
class PageSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("ƏSAS SƏHİFƏ META MƏLUMATLARI"), {'fields': ('logo', 'footer_logo', 'headerbgimg', 'favicon', 'title', 'description', 'keywords')}),
        (_("ƏLAQƏ MƏLUMATLARI"), {'fields': ('phone_number', 'email', 'address', 'footer_map', 'footer_map_link')}),
        (_("HAQQIMIZDA"), {'fields': ('about1', 'about2', 'about3', 'about4', 'about_img1', 'about_img2')}),
        (_("NİZAMNAMƏ"), {'fields': ('charter_img', 'charter')}),
        (_("QARABAĞ AZƏRBAYCANDIR!"), {'fields': ('karabakh',)}),
        (_("MƏDƏNİYYƏT"), {'fields': ('culture',)}),
        (_("TURİZM"), {'fields': ('tourism',)}),
    )
    inlines = [SocialMediaAccountAdmin]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

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

@admin.register(EBookModel)
class EBookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)

@admin.register(OfferModel)
class OfferAdmin(admin.ModelAdmin):
    readonly_fields = ("sent_date",)

@admin.register(IdeaModel)
class IdeaAdmin(admin.ModelAdmin):
    readonly_fields = ("sent_date",)

@admin.register(PhotoModel)
class IdeaAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)

admin.site.register(NewsTypeModel)
admin.site.register(NewsCategoryModel)
admin.site.register(NewsModel)
admin.site.register(FAQsModel)
admin.site.register(OfferQuestionModel)
admin.site.register(VolunteersModel)
admin.site.register(EventModel)
admin.site.register(VolunteerModel)
admin.site.register(DirectorModel)
admin.site.register(PartnerModel)
admin.site.register(PhotosModel)


AdminSite.site_title = _("GTIB sayt administrasiyası")
AdminSite.site_header = _("GTIB administrasiyası")
AdminSite.index_title = _("GTIB administrasiyası")