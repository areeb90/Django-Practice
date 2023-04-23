from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),
    path('add_emp/', add_emp, {}),
    path('del_emp/<int:emp_id>', del_emp),
    path('edit_emp/<int:emp_id>', edit_emp),
    path('update_emp/<int:emp_id>', update_emp),
]
