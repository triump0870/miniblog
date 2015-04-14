from django.contrib import admin
from .models import Post, Vote
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.
class PostAdmin(MarkdownModelAdmin):
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

class VoteAdmin(admin.ModelAdmin):
	pass

admin.site.register(Vote, VoteAdmin)