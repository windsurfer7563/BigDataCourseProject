# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm
from django.conf import settings
import os
from .prediction_func import cinemas_predict
import pandas as pd
import os, random, string



# Create your views here.
def index(request):
    return render(request, 'predict/index.html')

def results(request):
    response = "You're looking at the results of prediction."
    return HttpResponse(response)

def make_prediction(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            name_path, file_name = handle_uploaded_file(request.FILES['csv_file'])
            result, df = cinemas_predict(name_path)
            os.remove(name_path)
            if result: return HttpResponse("Error...")

            df.sort_index(inplace = True)

            result_file = os.path.join(settings.MEDIA_ROOT, file_name)
            df.to_csv(result_file)
            result_file_url = settings.MEDIA_URL + file_name

            context = {'data': [(key,value) for key,value in zip(df.index, df)],'result_file': result_file_url}



            return render(request, 'predict/results.html', context)

            #return HttpResponseRedirect('/predict/results/')
        else:
            return HttpResponse("Error...")

def handle_uploaded_file(f):
    file_name = f.name

    length = 13
    chars = string.ascii_letters + string.digits + '!@$^&*'
    random.seed = (os.urandom(1024))
    a = ''.join(random.choice(chars) for i in range(length))

    file_name, exts = os.path.splitext(file_name)
    file_name = '%s%s%s' % (file_name,str(a), exts)

    name_path = os.path.join(settings.TEMP_DIR, file_name)
    with open(name_path, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return name_path, file_name
