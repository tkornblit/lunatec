from models import *
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
	prepoulated_fields = {"slug" : ("name",)}
	list_display = ('name',)

class SubCategoryAdmin(admin.ModelAdmin):
	prepoulated_fields = {"slug" : ("name",)}
	list_display = ('name','category')

admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product)

