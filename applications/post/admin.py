from django.contrib import admin

from applications.post.models import Post, Comment, PostImage, Like

class ImageInlineAdmin(admin.TabularInline):
    model = PostImage
    fields = ("image",)
    max_num = 5

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "like_count"]
    list_filter = ["owner"]
    search_fields = ["title"]

    def like_count(self, obj):
        return obj.likes.filter(is_like=True).count()

# admin.site.register(Post)
# admin.site.register(PostImage)
admin.site.register(Comment)