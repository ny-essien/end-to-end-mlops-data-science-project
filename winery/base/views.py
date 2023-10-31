from django.shortcuts import render
import os 
import numpy as np
import pandas as pd
from machine_learning_project.pipeline.prediction import PredictionPipeline

# Create your views here.

def homepage(request):
    return render(request, 'base/index.html', context= {'name' : 'Nsikan'} )


def predict(request):

    pass


def results(request):
    pass

