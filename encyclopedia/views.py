from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
	if util.get_entry(entry):
		return render(request, "encyclopedia/entry.html", {
			"arcticle": Markdown().convert(util.get_entry(entry)),
			"title": entry
			})
	#return HttpResponseNotFound("<h1>Page not found</h1>")
	raise Http404("Page not found")