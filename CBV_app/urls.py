from django.urls import path
from .views import ( IndexView, 
                    studentListView, 
                    SchoolDetailView, 
                    SchoolFormView, 
                    SuccessPageView )

urlpatterns = [
    path('content/', IndexView.as_view(), name = 'template'),
    path('list_view/', studentListView.as_view(), name = 'studentlist'),
    path('school_list/<int:pk>/', SchoolDetailView.as_view(), name = 'studentdetail'),
    path('school_form/', SchoolFormView.as_view(), name = 'school form'),
    path('thanks/', SuccessPageView.as_view(), name='success_page'),

]