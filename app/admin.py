from django.contrib import admin
from .models import Category,TaggList,Product
# Register your models here.

admin.site.register(Category)
admin.site.register(TaggList)
admin.site.register(Product)
