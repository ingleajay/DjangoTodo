
from django.contrib import admin
from django.urls import path ,include
from TODO import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('accounts/', include('allauth.urls')),
    path('delete/<int:id>/', v.delete_task, name="delete"),
    path('edit/<int:id>/',v.edit_task,name="edit")
]
