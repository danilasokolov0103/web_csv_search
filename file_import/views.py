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
            request.session['filename'] = uploaded_file.name
        
            if not uploaded_file.name.endswith('.csv'):
                messages.error(request, 'THIS IS NOT A CSV FILE')
                
            else:
            

                fs = FileSystemStorage()
                
                saved_file = fs.save(uploaded_file.name, uploaded_file)
                filename = fs.path(uploaded_file.name)
                print(filename)
               
                filepath = fs.path(saved_file)
                
                
                request.session['data'] = import_csv.import_from_csv(filepath)
                fs.delete(uploaded_file.name)
                return HttpResponseRedirect('find/')
        return render(request, 'upload.html', context )
    return render(request, 'upload.html', context )      
   


def find(request):
    context = {}
    filename = request.session['filename']
    if request.method == 'POST':
            
            fname = request.POST.get('fname',False)
            lname = request.POST.get('lname',False)
            print(fname)
            print(lname)
            context['fname'] = fname
            context['lname'] = lname  
            employ = request.session['data']
            
            print(filename)
            context['filename'] = filename

            context['info'] = find_info.show_info(employ,fname,lname)
            if len(context['info']) == 0:
                context['info'] = 'Таких сотрудников нет'
                messages.success(request,context['info'])
            else:
                for i in context['info']:
                    messages.success(request,i)
            return render(request, 'find.html', context = {'filename':filename,'fname':fname,'lname':lname})
    return render(request, 'find.html',context = {'filename':filename})
        

