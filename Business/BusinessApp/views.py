from django.views.generic import (CreateView, ListView,
                                  UpdateView, DeleteView)
from .forms import BusinessModelForm
from .models import Business
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())

class MyLoginView(SuccessMessageMixin, LoginView):
    redirect_authenticated_user = True
    success_message = "User Login successfull"

    def get_success_url(self):
        return reverse_lazy('home') 
    
class HomePageView(LoginRequiredMixin, ListView):
    context_object_name = 'business'
    model = Business
    template_name = 'business_detail_form.html'
    queryset = Business.objects.all().order_by('organisation_name')
    paginate_by = 5
    
class BusinessListView(SuccessMessageMixin, LoginRequiredMixin, ListView):
    context_object_name = 'business'
    model = Business
    template_name = 'business_detail_form.html'

    def get_queryset(self):
        search = self.request.GET.get('search', ' ') 
        return Business.objects.filter(organisation_name__icontains=search).order_by('organisation_name')

class BusinessCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Business
    template_name = 'business_create_form.html'
    form_class = BusinessModelForm
    success_url = reverse_lazy('home')
    success_message = "Record was created successfully"

class BusinessUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Business
    template_name = 'business_edit_form.html'
    form_class = BusinessModelForm
    success_url = reverse_lazy('home')
    success_message = "Record was updated successfully"

class BusinessDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Business
    template_name = 'business_delete_form.html'
    success_url = reverse_lazy('home')
    success_message = "Record was deleted successfully"