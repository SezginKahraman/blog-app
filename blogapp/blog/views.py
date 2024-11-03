from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog, Category

# Create your views here.
# def index(request):
#     return render(request, "blog/index.html")

dataJson = {
    "blogs": [
        {
            "id": 1,
            "title": "Web Geliştirme",
            "image": "web_gelistirme.jpg",
            "is_active": True,
            "is_homepage": True,
            "description": "çok iyi bir kurs",
        },
        {
            "id": 2,
            "title": "Angular",
            "image": "angular.jpg",
            "is_active": True,
            "is_homepage": True,
            "description": "çok iyi bir kurs",
        },
        {
            "id": 3,
            "title": "Javascript kursu",
            "image": "javascript.jpg",
            "is_active": True,
            "is_homepage": True,
            "description": "çok iyi bir kurs",
        },
        {
            "id": 4,
            "title": "Node kursu",
            "image": "node-js.jpg",
            "is_active": True,
            "is_homepage": True,
            "description": "çok iyi bir kurs",
        },
        {
            "id": 5,
            "title": "Python kursu",
            "image": "python.jpg",
            "is_active": False,
            "is_homepage": False,
            "description": "çok iyi bir kurs",
        },
    ]
}


def index(request):
    # all = Blog.objects.all()  # select * from blog
    context = {
        "blogs": Blog.objects.filter(is_homepage=True, is_active=True),
        "categories": Category.objects.all(),
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all(),
    }
    return render(request, "blog/blogs.html", context)


def blogs_by_category(request, slug):
    context = {
        "blogs": Blog.objects.filter(category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category": slug,
    }
    return render(request, "blog/blogs.html", context)


def blog_details_with_id(request, id):
    data = Blog.objects.all()

    # db'den gelen nesne json objesi değil python objesidir. Bu yüzden o nesnenin property'si üzerinden değere erişmek gerekir. !
    selectedBlogFromDb = [blog for blog in data if blog.id == id][0]

    # Json objesi üzerinden işlem yapmak için index scripti kullanmak gerekir. blog["id"] gibi
    selectedBlogFromJson = [
        blogJson for blogJson in dataJson["blogs"] if blogJson["id"] == id
    ]

    blog = Blog.objects.get(id=id)
    return render(request, "blog/blog-details.html", {"blog": blog})

    # for blog in data["blogs"]:
    #     if blog["id"] == id:
    #         return render(request, "blog/blog-details.html", {"blog": blog})
    # return HttpResponse("Blog bulunamadı")


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {"blog": blog})
