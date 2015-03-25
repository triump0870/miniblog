from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	date_hierarchy = "created_at"
	#fields = ("title","published")
	# pass
admin.site.register(Post, PostAdmin)