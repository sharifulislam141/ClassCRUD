from django.urls import path
from MyApp import views

app_name = "my_app"
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('add_musician/',views.AddMusician.as_view(),name="add_musician"),
    path('update_musician/<int:pk>/',views.UpdateMusician.as_view(),name="update_musician"),
    path('delete_musician/<int:pk>/',views.DeleteMusician.as_view(),name="delete_musician")
]
