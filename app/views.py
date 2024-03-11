from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post

"""
    Routes and Rendering
"""

def index(request):
    return render(request, "index.html")

def loginView(request):
    pass

def signupView():
    pass

@login_required
def feedView(request):
    pass

@login_required
def profileView(request):
    pass

@login_required
def detailedPostView(request, post_id):
    return render(request, "post.html", { "id": post_id })


"""
    API Functions
"""
# @login_required
def getPost(request, post_id, *args, **kwargs):
    data = {
        "id": post_id,
        "status": None,
    }

    try:
        postObj = Post.objects.get(id=post_id)

        data["status"] = 200
        data["message"] = "Post found successfully!"
        data["author"] = postObj.author
        data["content"] = postObj.content
        data["date"] = postObj.date
    except Exception as e:
        data["status"] = 404
        data["message"] = "Post not found!"
    
    return JsonResponse(data, status=data["status"])