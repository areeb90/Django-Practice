from django.http import HttpResponse
from django.shortcuts import render


import datetime


def home(request):

    isActive = False

    if request.method == 'POST':
        check = request.POST.get('check')
        if check == "True":

            isActive = True

            print(check)
            print(isActive)
        # print(request.method)

    else:
        isActive = False

    date = datetime.datetime.now()

    name = 'Areeb'

    list_of_courses = [
        'Python', 'Django', 'MySQL', 'Redis', 'Git', 'Java', 'C++', 'OS', 'Node'
    ]

    data = {
        'date': date,


        # boolean value, True or False. Default is True.
        'is_active': isActive,


        'name': name, 		# string value. Default is '' (empty string).

        # list of strings. Default is an empty list.
        'list_of_courses': list_of_courses,
    }

    # print("Home func is called")
    # return HttpResponse("<h1>This is the response from the test function</h1>")
    return render(request, "home.html", data)


def about(request):
    # this is the same as above, just without the template name. 	# the template name is optional. 	return HttpResponse("<h1>This is the about page</h1>")
    return render(request, "about.html", {})


def index(request):
    # response is the HttpResponse object from the home.html template file.
    return HttpResponse("<h1>This is the index function</h1>")
