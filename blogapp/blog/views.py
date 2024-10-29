from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
# def index(request):
#     return render(request, "blog/index.html")

data = {
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
    context = {"blogs": data["blogs"]}
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {"blogs": data["blogs"]}
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    selectedBlog = [blog for blog in data["blogs"] if blog["id"] == id][0]
    return render(request, "blog/blog-details.html", {"blog": selectedBlog})

    # for blog in data["blogs"]:
    #     if blog["id"] == id:
    #         return render(request, "blog/blog-details.html", {"blog": blog})
    # return HttpResponse("Blog bulunamadı")
