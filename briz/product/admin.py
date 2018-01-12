from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin
from .models import Dress, Seremoni, Skjorte, Sko, Smoking, Slips, Sloyfe, Mansjett, NewsImage, IndexContent, IndexProduct, Tip, Contact, Dressen_sitte, Dress_guide, Collection

class IndexContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(IndexContent, IndexContentAdmin)

# Register your models here.
admin.site.register(NewsImage)
admin.site.register(IndexProduct)
admin.site.register(Dress)
admin.site.register(Seremoni)
admin.site.register(Skjorte)
admin.site.register(Sko)
admin.site.register(Smoking)
admin.site.register(Slips)
admin.site.register(Sloyfe)
admin.site.register(Mansjett)
admin.site.register(Contact)
admin.site.register(Dressen_sitte)
admin.site.register(Dress_guide)

admin.site.register(Collection)


class TipAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(Tip, TipAdmin)