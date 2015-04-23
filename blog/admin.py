from django.contrib import admin
from .models import Post, Tag, Project, Work, About,Skill, Education, Music, UserData, Language, Conference
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

# Simple Model admin
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Music)
admin.site.register(UserData)
admin.site.register(Language)

# Advanced Model Admin
class PostAdmin(MarkdownModelAdmin):
	date_hierarchy = "created_at"
	fields = ('published',"title","slug","content","author","tags")
	list_display = ["published","title","updated_at"]
	list_display_links = ["title"]
	list_editable = ["published"]
	list_filter = ["published","updated_at","author","tags"]
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ["^title","^content"]

admin.site.register(Post, PostAdmin)

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

class EducationAdmin(admin.ModelAdmin):
	date_hierarchy = "start_date"
	fields = ('published','start_date','end_date','course', 'institution', 'website', 'mode')
	list_display = ['published','course','is_present']
	list_display_links = ['course']
	list_filter = ['course','institution']
	search_fields = ['^course','^institution','end_date']

admin.site.register(Education,EducationAdmin)

class ConferenceAdmin(admin.ModelAdmin):
	fields = ('published','date','name', 'place', 'link')
	list_display = ['published','name','date','link']
	list_display_links = ['name','link']
	list_filter = ['name','place']
	search_fields = ['^name','^place']

admin.site.register(Conference,ConferenceAdmin)