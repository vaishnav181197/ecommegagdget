from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from django.urls import reverse_lazy
from .forms import LogForm,RegForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Product
# Create your views here.
# class LogView(View):
#     def get(self,request):
#         form=LogForm()
#         return render(request,"log.html",{"form":form})
#     def post(self,request):
#         form=LogForm(data=request.POST)
#         if form.is_valid():
#             uname=form.cleaned_data.get('username')
#             pswd=form.cleaned_data.get('password')
#             user=authenticate(request,username=uname,password=pswd)
#             if user:
#                 messages.success(request,"login Successfull!!")
#                 return redirect('home')
#             else:
#                 messages.error(request,"Invalid Username or Password!!")
#                 return redirect('log')
#         return render(request,"log.html",{"form":form})

class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request):
        form=LogForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pswd=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"login Successfull!!")
                return redirect('home')
            else:
                messages.error(request,"Invalid Username or Password!!")
                return redirect('log')
        return render(request,"log.html",{"form":form})
    

# class RegView(View):
#     form_class=RegForm
#     template_name="reg.html"
#     model=User
#     success_url="log"
#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{"form":form})
#     def post(self,request):
#         form_data=self.form_class(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"Registration Successfull!!")
#             return redirect(self.success_url)
#         messages.error(request,"Validation Failed!!")
#         return render(request,self.template_name,{"form":form_data})

class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy("log")
    def form_valid(self, form):
        messages.success(self.request,"Registration Success")
        return super().form_valid(form)


# class HomeView(TemplateView):
#     template_name="home.html"

class HomeView(ListView):
    template_name="home.html"
    queryset=Product.objects.all()
    context_object_name="data"


class LgOutView(View):
    def get(self,request):
        logout(request)
        return redirect('log')