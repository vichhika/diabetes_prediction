from os import PRIO_PROCESS
from django.shortcuts import render
from django.utils.html import strip_tags
import numpy as np
import joblib
# Create your views here.
lr_model = joblib.load('./model/diabetes_model.joblib')

def home(request):
    if request.method == 'POST':
        try:
            test = [
                int(request.POST['pregancies']),
                int(request.POST['glucose']),
                int(request.POST['bloodPressure']),
                int(request.POST['skinThickness']),
                int(request.POST['insulin']),
                float(request.POST['weight'])/(float(request.POST['height'])**2),
                float(request.POST['diabetesPedigree']),
                int(request.POST['age'])
            ]
            outcome = lr_model.predict([test])[0]
            return render(request,'home.html',{'outcome':outcome})
        except:
            return render(request,'home.html',{'outcome':2})
    return render(request,'home.html',{})