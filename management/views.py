from django.shortcuts import render, redirect,HttpResponse
from django.shortcuts import render,get_object_or_404
from management.forms import EmployeForm, ManagerForm,CreateUserForm
from .models import Employe, Managerr
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

#Main Page
def main_page(request):
    return render(request,'management/login.html')

#Manager Dashboard
def home(request):
    if request.user.is_authenticated:
        emp= Employe.objects.all().order_by('firstname', 'lastname')
        form = EmployeForm()
        if request.method == 'POST':
            form = EmployeForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()
                form = EmployeForm()
                return redirect('home')
            else:
                form = EmployeeForm()
        
        context = {'form': form,
                    'emp': emp }
        return render(request,'management/home.html',context)
    else:
        return redirect('main_page')


#Employee Deletion
def delete_emp(request, qid):
    if request.user.is_authenticated:
        delete = Employe.objects.filter(empId=qid)
        delete.delete()
        return redirect('home')
    else:
        return redirect('main_page')

#Edit Employee Information
def edit_emp(request, qid):
    if request.user.is_authenticated:
        item = Employe.objects.get(empId=qid)
        editform = EmployeForm(instance=item)
        if request.method == "POST":
            editform = EmployeForm(request.POST, instance=item)
            if editform.is_valid():
                editform.save()
                return redirect('home')
            else:
                return redirect('main_page')
        context = {
                'editform': editform
                }
        return render(request,'management/edit.html',context)
    else:
        return redirect('main_page')



def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    context = {'form': form}
    return render(request, 'management/register.html', context)




def managerProfile(request):
    user = request.user
    if user.is_authenticated:
        emp= Employe.objects.all().order_by('firstname', 'lastname')
        manaform = ManagerForm()
        if request.method == 'POST':
            manaform = ManagerForm(request.POST)
            if manaform.is_valid():
                manaform = manaform.save(commit=False)
                manaform.firstname = request.user.first_name
                manaform.lastname = request.user.last_name
                manaform.email = user.email
                manaform.save()
                manaform = ManagerForm()
                return redirect('home')
            else:
                manaform = ManagerForm()
        
        context = {'manaform': manaform }
        return render(request,'management/profile.html',context)
    else:
        return redirect('main_page')
    