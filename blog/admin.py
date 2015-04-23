from django.contrib import admin
from .models import Post, Vote, Tag, Project, Work, About,Skill
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.
class PostAdmin(MarkdownModelAdmin):
	date_hierarchy = "created_at"
	fields = ('published',"title","slug","content","image","author","tags")
	list_display = ["published","title","updated_at"]
	list_display_links = ["title"]
	list_editable = ["published"]
	list_filter = ["published","updated_at","author","tags"]
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ["^title","^content"]

	# pass
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Skill)
class VoteAdmin(admin.ModelAdmin):
	pass

admin.site.register(Vote, VoteAdmin)
# class CommentAdmin(admin.ModelAdmin):
# 	pass
# admin.site.register(Comment,CommentAdmin)

class ProjectAdmin(MarkdownModelAdmin):
	date_hierarchy = "date"
	fields = ('published','date','title','slug','content','image','url','github')
	list_display = ['published','title','date']
	list_display_links = ['title']
	list_editable = ['published']
	list_filter = ['published', 'date',]
	prepopulated_fields = {'slug':('title',)}
	search_fields = ['^title','^content']

admin.site.register(Project, ProjectAdmin)

class WorkAdmin(MarkdownModelAdmin):
	date_hierarchy = "start_date"
	fields = ('start_date','end_date','company','designation','content')
	list_display = ['company','designation','span']
	list_filter = ['company','designation']
	search_fields = ['^company','^designation']

admin.site.register(Work, WorkAdmin)