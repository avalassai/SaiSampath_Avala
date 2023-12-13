from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm

def home(request):
    records = Record.objects.all()

    return render(request,'home.html',{'records':records})


def UserLogin(request):
    pass



def CustomerRecord(request , pk):
    customer_record = Record.objects.get(id=pk)
    return render(request, 'record.html',{'customer_record':customer_record})


def DeletePage(request ,pk):
    customer_record = Record.objects.get(id=pk)
    return render(request, 'delete.html',{'customer_record':customer_record})



def DeleteRecord(request,pk):
    delete_rec = Record.objects.get(id=pk)
    delete_rec.delete()
    messages.success(request,"You have Deleted the record")
    return redirect('home')
        
def AddRecord(request):
    
    form = AddRecordForm(request.POST or None)
    if request.method =="POST":
        if form.is_valid():
            add_record =  form.save()
            messages.success(request,"Record Added")
            return redirect('home')

    return render(request, 'AddContact.html',{'form':form})



def UpdateRecord(request,pk):
    cust_record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None , instance = cust_record)
    if form.is_valid():
        form.save('home')
        messages.success(request,"Record has been updated")
        return redirect('home')
    return render(request, 'UpdateRecord.html',{'form':form})










