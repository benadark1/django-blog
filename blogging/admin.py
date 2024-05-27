from django.contrib import admin
from blogging.models import Post, Category

# a new admin registration
admin.site.register(Post)
# new admin registration for Category Model
admin.site.register(Category)
