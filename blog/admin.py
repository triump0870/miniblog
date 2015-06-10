from django.contrib import admin
from .models import Post, Tag, Project, Work, About,Skill, Education, Music, UserData, Language, Conference, Contact, Image
from django_markdown.admin import MarkdownModelAdmin

# Simple Model admin
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Music)
admin.site.register(Language)
admin.site.register(Contact)

# Advanced Model Admin
class PostAdmin(MarkdownModelAdmin):
	actions = ['make_published']

	# Actions methods
	def make_published(self, request, queryset):
		rows_updated = queryset.update(status='p')
		if rows_updated == 1:
		    message_bit = "1 post was"
		else:
		    message_bit = "%s posts were" % rows_updated
		self.message_user(request, "%s successfully marked as published." % message_bit)

	make_published.short_description = "Mark selected stories as published"
	date_hierarchy = "created_at"
	# fields = ('status',"title","slug","content","author","tags")
	list_display = ["title","updated_at","status"]
	list_display_links = ["title"]
	list_filter = ["status","updated_at","author","tags"]
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ["^title","^content"]

admin.site.register(Post, PostAdmin)

class ProjectAdmin(MarkdownModelAdmin):
	actions = ['make_published']

	# Actions methods
	def make_published(self, request, queryset):
		rows_updated = queryset.update(status='p')
		if rows_updated == 1:
		    message_bit = "1 project was"
		else:
		    message_bit = "%s projects were" % rows_updated
		self.message_user(request, "%s successfully marked as published." % message_bit)

	make_published.short_description = "Mark selected stories as published"
	date_hierarchy = "date"
	fields = ('status','date','title','slug','subtitle','content','image','side_image','url','github')
	list_display = ['status','title','date']
	list_display_links = ['title']
	# list_editable = ['status']
	list_filter = ['status', 'date',]
	prepopulated_fields = {'slug':('title',)}
	search_fields = ['^title','^content']

admin.site.register(Project, ProjectAdmin)

class WorkAdmin(MarkdownModelAdmin):
	date_hierarchy = "start_date"
	fields = ('start_date','end_date','company','website','designation','content')
	list_display = ['company','designation','span']
	list_filter = ['company','designation']
	search_fields = ['^company','^designation']

admin.site.register(Work, WorkAdmin)

class EducationAdmin(admin.ModelAdmin):
	date_hierarchy = "start_date"
	fields = ('status','start_date','end_date','course', 'institution', 'website', 'mode')
	list_display = ['status','course','is_present']
	list_display_links = ['course']
	list_filter = ['course','institution']
	search_fields = ['^course','^institution','end_date']

admin.site.register(Education,EducationAdmin)

class ConferenceAdmin(admin.ModelAdmin):
	fields = ('status','date','name', 'place', 'link')
	list_display = ['status','name','date','link']
	list_display_links = ['name','link']
	list_filter = ['name','place']
	search_fields = ['^name','^place']

admin.site.register(Conference,ConferenceAdmin)

class UserDataModelAdmin(admin.ModelAdmin):
	list_display = ['fullname','user', 'role']

admin.site.register(UserData, UserDataModelAdmin)

class ImageModelAdmin(admin.ModelAdmin):
	list_display = ['about_image','blog_image','contact_image']
	list_display_links = ['about_image','blog_image','contact_image']

admin.site.register(Image,ImageModelAdmin)