from django.contrib import admin
from main.models import Post, Img
from django.forms import TextInput, Textarea
from django.db import models

admin.site.register(Img)
class ImgInline(admin.TabularInline):
    model = Img
    extra = 3 

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]
    list_filter = ["date"]
    search_fields = ["title"]
    formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'size':'150'})},
    models.TextField: {'widget': Textarea(attrs={'rows':30, 'cols':150})},
    }   
    inlines = [ ImgInline, ]
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Post, PostAdmin)