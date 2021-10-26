

# Register your models here.
from django.contrib import admin
from .models import GeeksModel

@admin.register(GeeksModel)
class GeeksModelAdmin(admin.ModelAdmin):
    list_display=['id','title','description','price','image_main','image_1','image_2','image_link','image_link_1','image_link_2','category','countInStock']
