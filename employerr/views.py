from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView

# Create your views here.
from employerr.models import Jobs
from django.contrib.auth import authenticate

from employerr.forms import SignUp
from employerr.forms import LoginForm,PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout

from employerr.forms import JobForm
class EmployerHomeView(TemplateView):
    template_name="emp-home.html"

class AddJobView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = 'emp-addjob.html'
    success_url = reverse_lazy('emp-alljobs')

    #2
    # def get(self,request):
    #     form=JobForm()
    #     return render(request,"emp-addjob.html",{"form":form})
    # def post(self,request):
    #     form=JobForm(request.POST)
    #     if form.is_valid():


            #1
            # jobname=form.cleaned_data.get("job_title")
            # cname=form.cleaned_data.get("company_name")
            # location=form.cleaned_data.get("location")
            # salary=form.cleaned_data.get("salary")
            # exp=form.cleaned_data.get("experience")
            #
            # Jobs.objects.create(
            #     job_title=jobname,
            #     company_name=cname,
            #     location=location,
            #     salary=salary,
            #     experience=exp
            # )
            # return render(request,"emp-home.html")
            #     return redirect("emp-alljobs")
            # else:
            #     return render(request,"emp-addjob.html",{"form":form})

        #2
        #     form.save()
        #     # return render(request,"emp-home.html")
        #     return redirect("emp-alljobs")
        # else:
        #     return render(request,"emp-addjob.html",{"form":form})

class ListJobView(ListView):
    model=Jobs
    context_object_name = "jobs"
    template_name = "emp-listjobs.html"
    # def get(self, request):
    #     qs = Jobs.objects.all()
    #     return render(request,"emp-listjobs.html",{"jobs":qs})


class JobDetailView(DetailView):
    model=Jobs
    context_object_name = 'jobs'   #{'jobs':qs}=key used
    template_name = 'emp-detailjob.html'
    pk_url_kwarg = "id"

    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,"emp-detailjob.html",{"job":qs})


class JobEditView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = 'emp-editjob.html'
    success_url = reverse_lazy('emp-alljobs')
    pk_url_kwarg = "id"

    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(instance=qs)
    #     return render(request,"emp-editjob.html",{"form":form})
    # def post(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("emp-alljobs")
    #     else:
    #         return render(request,'emp-editjob.html',{'form':form})

class JobDeleteView(DeleteView):
    template_name = "jobconfirmdelete.html"
    success_url = reverse_lazy('emp-alljobs')
    pk_url_kwarg = 'id'
    model = Jobs


    # def get(self,requst,id):
    #     qs=Jobs.objects.get(id=id)
    #     qs.delete()
    #     return redirect("emp-alljobs")
class SignUpView(CreateView):
    model=User
    form_class = SignUp
    template_name = "usersignup.html"
    success_url = reverse_lazy("emp-alljobs")

class SignInView(FormView):
    form_class = LoginForm
    template_name = "loggin.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)

                return redirect("emp-alljobs")
            else:
                return render(request,"loggin.html",{{"form":form}})

def SignOutView(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class ChangePasswordView(TemplateView):
    template_name = "changepassword.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
           return redirect('password-reset')

        else:
            return render(request,self.template_name)

class PasswordResetView(TemplateView):

    template_name = "passwordreset.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2=request.POST.get("pwd2")

        if pwd1 !=pwd2:
            return render(request,self.template_name,{'msg':'password mismatch'})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")




