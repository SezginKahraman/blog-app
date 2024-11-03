from django.contrib import admin

from .models import Blog, Category

# Özelleştirilmiş bir admin paneli modeli oluşturabiliriz.


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "is_homepage", "slug"]
    list_editable = [
        "is_active",
        "is_homepage",
    ]  # admin panelinde, nesnenin detayına girmeden, liste üzerinden editleyebilme özelliğinin hangi fieldlara ekleneceğini belirler.
    search_fields = [
        "title",
        "description",
    ]  # admin panelinde, arama yapılacak fieldları belirler.
    readonly_fields = ["slug"]  # admin panelinde, fieldların readonly olmasını sağlar.


admin.site.register(
    Blog, BlogAdmin
)  # BlogAdmin ile, blog'un istediğimiz fieldlarını liste üzerinde gösterebiliriz.

admin.site.register(Category)
