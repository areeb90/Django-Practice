from django.shortcuts import render, redirect

from .models import employee_MS

# Create your views here.


def home(request):

    emps = employee_MS.objects.all()

    return render(request, 'emp/home.html', {
        'emps': emps
    })


def add_emp(request):
    if request.method == "POST":

        # print("Post request lag gye areeb bhai")

        # data fetch
        name = request.POST.get('emp_name')
        # or request.POST['emp_dept']  # or request.POST
        dept = request.POST.get('emp_dept')
        # or request.POST['emp_sal']  # or request.POST  # or
        sal = request.POST.get('emp_sal')
        designation = request.POST.get('emp_desig')

        # create model obj and set the data

        e = employee_MS()
        e.name = name
        e.department = dept
        e.salary = sal
        e.designation = designation

        # save the object

        e.save()

        # display message

        print("Saved Details")

        return redirect("/emp/")
    return render(request, 'emp/add_emp.html', {})


def del_emp(request, emp_id):
    # print(emp_id)
    employee = employee_MS.objects.get(pk=emp_id)
    employee.delete()

    return redirect("/emp/")



def edit_emp(request, emp_id):
    emp = employee_MS.objects.get(pk=emp_id)



    return render(request, 'emp/edit.html', {
        'emp': emp,
    })



def update_emp(request, emp_id):

    if request.method == "POST":


    # data fetch
        name = request.POST.get('emp_name')
        # or request.POST['emp_dept']  # or request.POST
        dept = request.POST.get('emp_dept')
        # or request.POST['emp_sal']  # or request.POST  # or
        sal = request.POST.get('emp_sal')
        designation = request.POST.get('emp_desig')



        e = employee_MS()
        e.id = emp_id
        e.name = name
        e.department = dept
        e.salary = sal
        e.designation = designation


        e.save()

        return redirect("/emp/")  # or return HttpResponseRedirect("/emp/")  if you want to direct back to the same page



