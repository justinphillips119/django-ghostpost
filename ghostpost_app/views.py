from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost_app.models import GhostpostModel
from ghostpost_app.forms import GhostpostForm


def index(request):
    all_posts = GhostpostModel.objects.filter().order_by("-id")
    return render(request, "index.html", {"title": "Ghost Posts", "all_posts": all_posts})


def new_post_view(request):
    if request.method == "POST":
        form = GhostpostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostpostModel.objects.create(
                post_type = data.get("post_type"),
                content = data.get("content"),
                )
            return HttpResponseRedirect(reverse("homepage"))

    form = GhostpostForm()
    return render(request, "post.html", {"form": form, "newpost_title": "Add New Post"})


def boasts_view(request):
    boasts = GhostpostModel.objects.filter(post_type=True).order_by("-id")
    return render(request, "boasts.html", {"boasts_title": "Boasts", "boasts": boasts})


def roasts_view(request):
    roasts = GhostpostModel.objects.filter(post_type=False).order_by("-id")
    return render(request, "roasts.html", {"roasts_title": "Roasts", "roasts": roasts})


def votes_view(request):
    votes = sorted(GhostpostModel.objects.all(), key=lambda votes:votes.votes)[::-1]
    return render(request, "votes.html", {"votes_title": "Sorted By Number Of Votes", "votes": votes})


def upvote_view(request, post_id):
    post = GhostpostModel.objects.get(id=post_id)
    post.upvote += 1
    post.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def downvote_view(request, post_id):
    post = GhostpostModel.objects.get(id=post_id)
    post.downvote += 1
    post.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))





