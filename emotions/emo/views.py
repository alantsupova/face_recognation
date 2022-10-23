from django.shortcuts import render
from django.http import HttpResponse
from deepface import DeepFace
from .emotions_algo import *
import cv2
import time
# Create your views here.
def happy(request):
    cap = cv2.VideoCapture(0)
    success, img = cap.read()
    res = face_analize(img)
    context = {
        'emotion': res['dominant_emotion']
    }
    print(context)
    cap.release()
    cv2.destroyAllWindows()
    return render(request, 'index.html', context)



def test(request):
    cap = cv2.VideoCapture(0)
    success, img = cap.read()
    res = face_analize(img)
    context = {
        'emotion': res['dominant_emotion']
    }
    print(context)
    cap.release()
    cv2.destroyAllWindows()
    return render(request, 'emo/index.html', context)
