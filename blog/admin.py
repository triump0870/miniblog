from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	date_hierarchy = "created_at"
	fields = ('published',"title","slug","content","author")
	list_display = ["published","title","updated_at"]
	list_display_links = ["title"]
	list_editable = ["published"]
	list_filter = ["published","updated_at","author"]
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ["^title","^content"]

	# pass
admin.site.register(Post, PostAdmin)