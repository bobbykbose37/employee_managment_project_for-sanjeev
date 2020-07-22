from django.shortcuts import render,redirect
from .import models
from .models import user,complaint



# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        obj=user.objects.all()
        for i in obj:
            if i.name==username:
                if i.password==password:
                    obj=complaint.objects.all().filter(name=username)
                    return render(request,"admin_template.html",{'obj':obj})
    else:
        return render(request,"login.html")

def registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        listt = [9999]
        objj = user.objects.all()
        for i in objj:
            print("6666666666666", i.complaint_id)
            listt.append(int(i.complaint_id))
            print("ppppppppp",listt)
            complaint_idd = max(listt)
        listt = []
        # print("jjjjjjjjjjjjj", complaint_idd)
        obj=models.user()
        obj.name=username
        obj.password=password
        obj.complaint_id=complaint_idd+1
        obj.save()
        ooo=user.objects.all().filter(name=username)
        return render(request,'signup_details.html',{'obj':ooo})
    return render(request,"registration.html")

def admin_template(request):
    obj=complaint.objects.all()
    return render(request,"admin_template.html",{'obj':obj})

def employee_registration(request):
    if request.method=="POST":

        name=request.POST["name"]
        complaint_id = request.POST["complaint_id"]
        date = request.POST["date"]
        issue = request.POST["issue"]
        issue_type = request.POST["issue_type"]
        reported_by = request.POST["reported_by"]
        handled_by = request.POST["handled_by"]
        company_name = request.POST["company_name"]
        location = request.POST["location"]
        department = request.POST["department"]
        status = request.POST["status"]
        remarks = request.POST["remarks"]
        obj=models.complaint()
        obj.name=name
        obj.complaint_id=complaint_id
        obj.date=date
        obj.issue=issue
        obj.issue_type=issue_type
        obj.reported_by=reported_by
        obj.handled_by=handled_by
        obj.company_name=company_name
        obj.location = location
        obj.department = department
        obj.status = status
        obj.remarks = remarks
        obj.save()
        return redirect('admin_template')
    return render(request,"employee_registration.html")

def employee_edit_view(request):
    obj = complaint.objects.all()
    for i in obj:
        print("999999999999999999", i, i.date, obj)
    return render(request,"employee_edit_page.html",{'obj':obj})

def employee_registration_edit(request,sid):
    obj=complaint.objects.get(id=sid)
    if request.method == "POST":
        complaint_id = request.POST["complaint_id"]
        date = request.POST["date"]
        issue = request.POST["issue"]
        issue_type = request.POST["issue_type"]
        reported_by = request.POST["reported_by"]
        handled_by = request.POST["handled_by"]
        company_name = request.POST["company_name"]
        location = request.POST["location"]
        department = request.POST["department"]
        status = request.POST["status"]
        remarks = request.POST["remarks"]
        obj = complaint.objects.get(id=sid)
        obj.complaint_id = complaint_id
        obj.date = date
        obj.issue = issue
        obj.issue_type = issue_type
        obj.reported_by = reported_by
        obj.handled_by = handled_by
        obj.company_name = company_name
        print("entered 1")
        obj.location = location
        obj.department = department
        obj.status = status
        obj.remarks = remarks
        print("updted saved")
        obj.save()
        return redirect('menu')
    return render(request,"employee_edit_input.html",{'obj':obj})

def employee_delete_view(request):
    obj = complaint.objects.all()
    return render(request,"employee_delete_page.html",{'obj':obj})

def employee_registration_delete(request,sid):
    obj=complaint.objects.get(id=sid)
    obj.delete()
    return render(request,'menu.html')

def menu(request):
    return render(request,"menu.html")

def employee_search(request):
    obj=complaint.objects.all()
    if request.method=="POST":
        name=request.POST["name"]
        obj=complaint.objects.get(name=name)
        return render(request,"employee_search_show.html",{'obj':obj})
    return render(request,"employee_search.html",{'obj':obj})

