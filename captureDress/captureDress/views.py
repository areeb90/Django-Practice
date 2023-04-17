from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    print("test func is called")
    # return HttpResponse("<h1>This is the response from the test function</h1>")
    return render(request, "home.html", {})


def about(request):
    # this is the same as above, just without the template name. 	# the template name is optional. 	return HttpResponse("<h1>This is the about page</h1>")
    return render(request, "about.html", {})


def index(request):
    # response is the HttpResponse object from the home.html template file.
    return HttpResponse("<h1>This is the index function</h1>")
