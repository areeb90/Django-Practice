from django.shortcuts import render
from .models import Tests

# Create your views here.
def home(request):
    # print("Tesimonials")
    if request.method == "GET":


        test = Tests.objects.all()
        print(test)

        return render(request, 'testimonials/home.html', {
        'test':test
        })
