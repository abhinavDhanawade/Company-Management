from django.shortcuts import render, redirect,HttpResponse
from django.shortcuts import render,get_object_or_404
from management.forms import EmployeForm, ManagerForm
from .models import Employe, Managerr
from django.contrib.auth.models import User
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


#Signup
def handlesignup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if len(username) > 10:
            return redirect('main_page')
        if pass1 != pass2:
            return redirect('main_page')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name, myuser.last_name = fullname.split(" ")
        myuser.save()        
        return redirect('main_page')
    else:
        return HttpResponse('sorry')

#Login
def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername').lower()
        loginpass = request.POST.get('loginpass')
        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'main_page')
    else:
        return redirect('handlelogin')

#LogOut
def handlelogout(request):
    logout(request)
    return redirect('main_page')

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
                manaform.user = request.user.email
                manaform.save()
                manaform = ManagerForm()
                return redirect('home')
            else:
                manaform = ManagerForm()
        
        context = {'manaform': manaform }
        return render(request,'management/profile.html',context)
    else:
        return redirect('main_page')
    