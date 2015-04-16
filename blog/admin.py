from django.contrib import admin
from .models import Post, Vote, Tag, Comment
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.
class PostAdmin(MarkdownModelAdmin):
	date_hierarchy = "created_at"
	fields = ('published',"title","slug","content","author","tags")
	list_display = ["published","title","updated_at"]
	list_display_links = ["title"]
	list_editable = ["published"]
	list_filter = ["published","updated_at","author","tags"]
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ["^title","^content","^tags"]

	# pass
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

class VoteAdmin(admin.ModelAdmin):
	pass

admin.site.register(Vote, VoteAdmin)
class CommentAdmin(admin.ModelAdmin):
	pass
admin.site.register(Comment,CommentAdmin)

