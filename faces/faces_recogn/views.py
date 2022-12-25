from django.shortcuts import render
from django.http import HttpResponse
from deepface import DeepFace
from .deep_algo import *
import cv2
import time
import numpy as np
# Create your views here.


def main_page(request):
    return render(request, 'index.html')

def new_user(request):
    cap = cv2.VideoCapture(0)
    success, img = cap.read()
    cv2.imwrite('face.png', img)
    cap.release()
    cv2.destroyAllWindows()
    return render(request, 'new_user.html')

def check(request):
    cap = cv2.VideoCapture(0)
    success, img = cap.read()
    res = face_verify(img1=img, img2='face.png')
    context = {
        'res': res
    }
    cap.release()
    cv2.destroyAllWindows()
    return render(request, 'check.html', context)
