from empapi.views import TaskAPIView, EmployeDetailsAPIView
from django.urls import path
urlpatterns = [

    path('emplist', TaskAPIView.as_view()),
    path('details/<str:id>', EmployeDetailsAPIView.as_view())

]
