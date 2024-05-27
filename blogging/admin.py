from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.StackedInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


# a new admin registration
# admin.site.register(Post)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)  # excluding post field

# new admin registration for Category Model
# admin.site.register(Category)
