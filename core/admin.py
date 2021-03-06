"""
django imports
"""
from django import forms
from django.contrib.admin import ModelAdmin
from django.contrib.admin import site as admin_site
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from selectable.forms import ( 
    AutoCompleteSelectWidget,
    AutoCompleteSelectField,
    AutoCompleteSelectMultipleWidget,
    AutoCompleteSelectMultipleField,
)

"""
regluit imports
"""
from . import models
from regluit.core.lookups import (
    PublisherNameLookup,
    WorkLookup,
    OwnerLookup,
    EditionLookup
)



class ClaimAdminForm(forms.ModelForm):
    work = AutoCompleteSelectField(
            lookup_class=WorkLookup,
            widget=AutoCompleteSelectWidget(lookup_class=WorkLookup),
            required=True,
        )
    user = AutoCompleteSelectField(
            lookup_class=OwnerLookup,
            widget=AutoCompleteSelectWidget(lookup_class=OwnerLookup),
            required=True,
        )
    class Meta(object):
        model = models.Claim
        exclude = ()

class ClaimAdmin(ModelAdmin):
    list_display = ('work', 'rights_holder', 'status')
    date_hierarchy = 'created'
    form = ClaimAdminForm
    
class RightsHolderAdminForm(forms.ModelForm):
    owner = AutoCompleteSelectField(
            lookup_class=OwnerLookup,
            widget=AutoCompleteSelectWidget(lookup_class=OwnerLookup),
            required=True,
        )
    class Meta(object):
        model = models.RightsHolder
        exclude = ()

class RightsHolderAdmin(ModelAdmin):
    date_hierarchy = 'created'
    form = RightsHolderAdminForm

class AcqAdmin(ModelAdmin):
    readonly_fields = ('work', 'user', 'lib_acq', 'watermarked')
    search_fields = ['user__username']
    date_hierarchy = 'created'

class PremiumAdmin(ModelAdmin):
    list_display = ('campaign', 'amount', 'description')
    date_hierarchy = 'created'

class CampaignAdminForm(forms.ModelForm):
    managers = AutoCompleteSelectMultipleField(
            lookup_class=OwnerLookup,
            widget= AutoCompleteSelectMultipleWidget(lookup_class=OwnerLookup),
            required=True,
        )
    class Meta(object):
        model = models.Campaign
        fields = ('managers', 'name', 'description', 'details', 'license', 'activated', 'paypal_receiver', 
            'status', 'type', 'email', 'do_watermark', 'use_add_ask', )

class CampaignAdmin(ModelAdmin):
    list_display = ('work', 'created', 'status')
    date_hierarchy = 'created'
    search_fields = ['work']
    form = CampaignAdminForm
 
class WorkAdmin(ModelAdmin):
    search_fields = ['title']
    ordering = ('title',)
    list_display = ('title', 'created')
    date_hierarchy = 'created'
    fields = ('title', 'description', 'language', 'featured', 'publication_range',
        'age_level', 'openlibrary_lookup')

class AuthorAdmin(ModelAdmin):
    search_fields = ('name',)
    date_hierarchy = 'created'
    ordering = ('name',)
    exclude = ('editions',)

subject_authorities = (('','keywords'),('lcsh', 'LC subjects'), ('lcc', 'LC classifications'), ('bisacsh', 'BISAC heading'),  )
class SubjectAdminForm(forms.ModelForm):
    authority = forms.ChoiceField(choices=subject_authorities, required=False )
    class Meta(object):
        model = models.Subject
        fields = 'name', 'authority', 'is_visible'
    
    
class SubjectAdmin(ModelAdmin):
    search_fields = ('name',)
    date_hierarchy = 'created'
    ordering = ('name',)
    form = SubjectAdminForm
    
class EditionAdminForm(forms.ModelForm):
    work = AutoCompleteSelectField(
            lookup_class=WorkLookup,
            label='Work',
            widget=AutoCompleteSelectWidget(lookup_class=WorkLookup),
            required=True,
        )
    publisher_name = AutoCompleteSelectField(
            lookup_class=PublisherNameLookup,
            label='Publisher Name',
            widget=AutoCompleteSelectWidget(lookup_class=PublisherNameLookup),
            required=False,
        )
    class Meta(object):
        model = models.Edition
        exclude = ()
        
class EditionAdmin(ModelAdmin):
    list_display = ('title', 'publisher_name', 'created')
    date_hierarchy = 'created'
    ordering = ('title',)
    form = EditionAdminForm

class PublisherAdminForm(forms.ModelForm):
    name = AutoCompleteSelectField(
            lookup_class=PublisherNameLookup,
            label='Name',
            widget=AutoCompleteSelectWidget(lookup_class=PublisherNameLookup),
            required=True,
        )

    class Meta(object):
        model = models.Publisher
        exclude = ()
        
class PublisherAdmin(ModelAdmin):
    list_display = ('name', 'url', 'logo_url', 'description')
    ordering = ('name',)
    form = PublisherAdminForm

class PublisherNameAdmin(ModelAdmin):
    list_display = ('name', 'publisher')
    ordering = ('name',)
    search_fields = ['name']

class RelationAdmin(ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ['name']
    
class EbookAdmin(ModelAdmin):
    search_fields = ('edition__title','^url')  # search by provider using leading url
    list_display = ('__unicode__','created', 'user','edition')
    date_hierarchy = 'created'
    ordering = ('edition__title',)
    exclude = ('edition','user', 'filesize')

class EbookFileAdmin(ModelAdmin):
    search_fields = ('ebook__edition__title', 'source')  # search by provider using leading url
    list_display = ('created', 'format', 'ebook_link', 'asking')
    date_hierarchy = 'created'
    ordering = ('edition__work',)
    fields = ('file', 'format', 'edition_link', 'ebook_link', 'source')
    readonly_fields  = ('file', 'edition_link', 'ebook_link', 'ebook')
    def edition_link(self, obj):
        if obj.edition:
            link = reverse("admin:core_edition_change", args=[obj.edition_id]) 
            return u'<a href="%s">%s</a>' % (link,obj.edition)
        else:
            return u''
    def ebook_link(self, obj):
        if obj.ebook:
            link = reverse("admin:core_ebook_change", args=[obj.ebook_id]) 
            return u'<a href="%s">%s</a>' % (link,obj.ebook)
        else:
            return u''
    edition_link.allow_tags=True
    ebook_link.allow_tags=True


class WishlistAdmin(ModelAdmin):
    date_hierarchy = 'created'

class UserProfileAdmin(ModelAdmin):
    search_fields = ('user__username',)
    date_hierarchy = 'created'
    exclude = ('user',)

class GiftAdmin(ModelAdmin):
    list_display = ('to', 'acq_admin_link', 'giver', )
    search_fields = ('giver__username', 'to')
    readonly_fields = ('giver', 'acq',) 
    def acq_admin_link(self, gift):
        return "<a href='/admin/core/acq/%s/'>%s</a>" % (gift.acq_id, gift.acq)
    acq_admin_link.allow_tags = True

class CeleryTaskAdmin(ModelAdmin):
    pass    
    
class PressAdmin(ModelAdmin):
    list_display = ('title', 'source', 'date')
    ordering = ('-date',)

class WorkRelationAdminForm(forms.ModelForm):
    to_work = AutoCompleteSelectField(
            lookup_class=WorkLookup,
            label='To Work',
            widget=AutoCompleteSelectWidget(lookup_class=WorkLookup),
            required=True,
        )
    from_work = AutoCompleteSelectField(
            lookup_class=WorkLookup,
            label='From Work',
            widget=AutoCompleteSelectWidget(lookup_class=WorkLookup),
            required=True,
        )
    class Meta(object):
        model = models.WorkRelation
        exclude = ()

class WorkRelationAdmin(ModelAdmin):
    form = WorkRelationAdminForm
    list_display = ('to_work', 'relation', 'from_work')
    
class IdentifierAdminForm(forms.ModelForm):
    work = AutoCompleteSelectField(
            lookup_class=WorkLookup,
            label='Work',
            widget=AutoCompleteSelectWidget(lookup_class=WorkLookup, attrs={'size':60}),
            required=False,
        )
    edition = AutoCompleteSelectField(
            lookup_class=EditionLookup,
            label='Edition',
            widget=AutoCompleteSelectWidget(lookup_class=EditionLookup, attrs={'size':60}),
            required=True,
        )
    class Meta(object):
        model = models.Identifier
        exclude = ()

class IdentifierAdmin(ModelAdmin):
    form = IdentifierAdminForm
    list_display = ('type', 'value')
    search_fields = ('type', 'value')

class OfferAdmin(ModelAdmin):
    list_display = ('work', 'license', 'price', 'active')
    search_fields = ('work__title',)
    readonly_fields = ('work',)
    

admin_site.register(models.Acq, AcqAdmin)
admin_site.register(models.Author, AuthorAdmin)
admin_site.register(models.Badge, ModelAdmin)
admin_site.register(models.Campaign, CampaignAdmin)
admin_site.register(models.CeleryTask, CeleryTaskAdmin)
admin_site.register(models.Claim, ClaimAdmin)
admin_site.register(models.Ebook, EbookAdmin)
admin_site.register(models.EbookFile, EbookFileAdmin)
admin_site.register(models.Edition, EditionAdmin)
admin_site.register(models.Gift, GiftAdmin)
admin_site.register(models.Identifier, IdentifierAdmin)
admin_site.register(models.Offer, OfferAdmin)
admin_site.register(models.Premium, PremiumAdmin)
admin_site.register(models.Press, PressAdmin)
admin_site.register(models.Publisher, PublisherAdmin)
admin_site.register(models.PublisherName, PublisherNameAdmin)
admin_site.register(models.Relation, RelationAdmin)
admin_site.register(models.RightsHolder, RightsHolderAdmin)
admin_site.register(models.Subject, SubjectAdmin)
admin_site.register(models.UserProfile, UserProfileAdmin)
admin_site.register(models.Wishlist, WishlistAdmin)
admin_site.register(models.Work, WorkAdmin)
admin_site.register(models.WorkRelation, WorkRelationAdmin)

