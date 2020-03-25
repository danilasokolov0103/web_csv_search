import csv
import re
import os
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from . import import_csv,find_info 
import shutil




def index(request):
    context = {}

    if request.method == 'POST':
        if len(request.FILES) != 0:
            uploaded_file = request.FILES["csv_file"]
        
            if not uploaded_file.name.endswith('.csv'):
                messages.error(request, 'THIS IS NOT A CSV FILE')
                
            else:
            

                fs = FileSystemStorage()
                saved_file = fs.save(uploaded_file.name, uploaded_file)
                filename = fs.path(uploaded_file.name)
                print(filename)
               
                filepath = fs.path(saved_file)
                
                messages.success(request,f'You chose file {filename}')
                messages.success(request,'http//localhost:8000/find')
                request.session['data'] = import_csv.import_from_csv(filepath)
                return HttpResponseRedirect('find/')
        return render(request, 'upload.html', context )
    return render(request, 'upload.html', context )      
   


def find(request):
    context = {}
    if request.method == 'POST':
            fname = request.POST.get('fname',False)
            lname = request.POST.get('lname',False)
            print(fname)
            print(lname)
            context['fname'] = fname
            context['lname'] = lname  
            employ = request.session['data']
            context['info'] = find_info.show_info(employ,fname,lname)
            for i in context['info']:
                messages.success(request,i)
    return render(request, 'find.html', context )
        

