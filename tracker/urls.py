from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('add/',views.add_application,name='add_application'),
    path('edit/<int:id>/',views.edit_application,name='edit_application'),
    path('delete/<int:id>/',views.delete_application,name='delete_application'),
]