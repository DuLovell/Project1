from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, Http404, HttpResponse
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
	if util.get_entry(entry):
		return render(request, "encyclopedia/entry.html", {
			"article": Markdown().convert(util.get_entry(entry)),
			"title": entry
			})
	#return HttpResponseNotFound("<h1>Page not found</h1>")
	#raise Http404("Page not found")
	return render(request, "encyclopedia/error.html")

def search(request):
	q = request.POST.get("q")
	articles_list = util.list_entries()

	if util.get_entry(q):
		return redirect("encyclopedia:entry", entry=q)
	elif q in "".join(articles_list):
		return render(request, "encyclopedia/search_results.html", {
			"articles_list": articles_list,
			"q": q
			})
	else:
		return render(request, "encyclopedia/search_results.html", {
			"articles_list": [],
			"q": q
			})

def create(request):
	if request.method == "GET":
		return render(request, "encyclopedia/create.html")
	elif request.method == "POST":
		title = request.POST.get("title")
		content = request.POST.get("content")
		if title in util.list_entries():
			return render(request, "encyclopedia/create_error.html")
		# Add .md file to 'entries' folder
		util.save_entry(title, content)
		return redirect("encyclopedia:entry", entry=title)