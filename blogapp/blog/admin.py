from django.contrib import admin

from .models import Blog, Category
from django.utils.safestring import mark_safe

# Özelleştirilmiş bir admin paneli modeli oluşturabiliriz.


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "is_homepage", "slug", "selected_categories"]
    list_editable = [
        "is_active",
        "is_homepage",
    ]  # admin panelinde, nesnenin detayına girmeden, liste üzerinden editleyebilme özelliğinin hangi fieldlara ekleneceğini belirler.
    search_fields = [
        "title",
        "description",
    ]  # admin panelinde, arama yapılacak fieldları belirler.
    readonly_fields = ["slug"]  # admin panelinde, fieldların readonly olmasını sağlar.
    list_filter = [
        "categories",
        "is_active",
        "is_homepage",
    ]  # admin panelinde, filtreleme yapılacak fieldları belirler.

    # def selected_categories(self, obj):
    #     return ", ".join([category.name for category in obj.categories.all()])

    def selected_categories(self, obj):
        html = (
            "<ul>"
            + "".join(
                [f"<li>{category.name}</li>" for category in obj.categories.all()]
            )
            + "</ul>"
        )
        return mark_safe(html)


admin.site.register(
    Blog, BlogAdmin
)  # BlogAdmin ile, blog'un istediğimiz fieldlarını liste üzerinde gösterebiliriz.

admin.site.register(Category)
