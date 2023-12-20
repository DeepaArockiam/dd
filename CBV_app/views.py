from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "ray of sunshine"
        return context
    

from .models import School, Student

class studentListView(ListView):
    model = Student
    template_name = 'CBV_app/listview.html'
    context_object_name = 'student_list'
    
    
    
class SchoolDetailView(DetailView):
    model = School
    template_name = 'CBV_app/detailview.html' 
    # context_object_name = 'school_list'
    




from django.views.generic.edit import FormView
from .forms import SchoolForm
from django.urls import reverse_lazy

class SchoolFormView(FormView):
    template_name = 'CBV_app/school_form.html'  # Update with your actual template path
    form_class = SchoolForm
    success_url = reverse_lazy('success_page')   # Redirect to this URL upon successful form submission

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class SuccessPageView(TemplateView):
    template_name = 'CBV_app/success.html'
    
    
    