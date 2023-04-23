from django.shortcuts import render, redirect

# Create your views here.


def home(request):

    return render(request, 'emp/home.html', {})


def add_emp(request):
    if request.method == "POST":
        # data fetch

        # create model obj and set the data

        # save the object

        # display message

        return redirect("/emp/")
    return render(request, '/emp/add_emp.html ', {})
