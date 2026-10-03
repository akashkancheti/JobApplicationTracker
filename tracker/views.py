from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import JobApplication
from .forms import JobApplicationForm
from django.db.models import Q
def home(request):
    total_applications=JobApplication.objects.count()
    applications=JobApplication.objects.all()
    query = request.GET.get('q')
    if query:
        applications = applications.filter(
            Q(company__icontains=query) |
            Q(role__icontains=query)
        )
    status_filter = request.GET.get('status')

    if status_filter:
        applications = applications.filter(status=status_filter)
    applied_count=JobApplication.objects.filter(status='Applied').count()
    interview_count=JobApplication.objects.filter(status='Interview').count()
    offer_count=JobApplication.objects.filter(status='Offer').count()
    rejected_count=JobApplication.objects.filter(status='Rejected').count()
    if total_applications > 0:
        interview_rate = round((interview_count / total_applications) * 100)
    else:
        interview_rate = 0
    context={
        'total_applications':total_applications,
        'applications':applications,
        'applied_count':applied_count,
        'interview_count':interview_count,
        'offer_count':offer_count,
        'rejected_count':rejected_count,
        'query': query,
        'status_filter': status_filter,
        'interview_rate': interview_rate,
    }
    return render(request,'home.html',context)
def add_application(request):
    if request.method=='POST':
        form=JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=JobApplicationForm()
    context={
        'form':form
    }
    return render(request,'add_application.html',context)
def edit_application(request,id):
    application=get_object_or_404(JobApplication,id=id)
    if request.method=='POST':
        form=JobApplicationForm(request.POST,instance=application)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=JobApplicationForm(instance=application)
    context={
        'form':form
    }
    return render(request,'edit_application.html',context)
def delete_application(request,id):
    application=get_object_or_404(JobApplication,id=id)
    if request.method=='POST':
        application.delete()
        return redirect('home')
    context={
        'application':application
    }
    return render(request,'delete_application.html',context)