from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http.response import HttpResponse, Http404
from django.template import RequestContext, loader
from django.apps import apps
from django.views.generic import View
from django.core.urlresolvers import reverse

from .models import (PersonalInfo,
                     WorkHistory,
                     Volunteer,
                     Community,
                     Skills,
                     Certifications,
                     Education,
                     CoverLetter,
                     Reference,
                     Publication,
                     )

class PersonalInfoView(View):
    template_name = 'work_history/data_template.html'
    
    def get(self, request, First_Name, Last_Name):
    	data = get_object_or_404(PersonalInfo.objects.filter(Last_Name=Last_Name).filter(First_Name=First_Name)) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': data.__str__, 'ziplist': ziplist, 'update':data.get_update_url, 'delete':data.get_update_url})