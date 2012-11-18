from django.contrib import admin
from lebron.models import Entry,Category

class AdminModel(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Entry, AdminModel)
admin.site.register(Category,AdminModel)