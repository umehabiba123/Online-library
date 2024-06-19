from django.contrib import admin
from .models import Books, Review
# Register your models here.
@admin.register(Books)
class BookAdminModel(admin.ModelAdmin):
    list_display = ["title", "author", "description", "date", "image"]

@admin.register(Review)
class ReviewsAdminModel(admin.ModelAdmin):
    list_display = ["book", "user", "review_text", "created_at"]
