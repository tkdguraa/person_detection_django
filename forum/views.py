from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip

import base64
import io
import cv2
import time
import os
from jinja2 import Environment, FileSystemLoader
from django.template import Context, loader
from darkflow.net.build import TFNet
# from django.contrib.auth.models import User

# Create your views here.
def post_list(request):
    print('!!!!!!!!!!!!x: ', x)
    return render(request, 'post_list.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

def display(request):
    img_str = base64.b64encode(b"")
    
    return render(request, 'post_list.html', {'img_str': img_str})

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()

    def get_frame(self):
        _, image = self.video.read()
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @gzip.gzip_page
def detect(request):
    # return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    return StreamingHttpResponse(run_darkflow(), content_type="multipart/x-mixed-replace;boundary=frame")

def video(request):
    return render(request, 'video.html', {})

# def detect(request):    
#     template = 'post_list.html'
#     context = get_sample_context()
#     stream = jinja_generate_with_template(template, context)
    
#     return StreamingHttpResponse(stream)

def simulate_long_response_with_delay():
    for i in range(5):
        time.sleep(1)
        yield 'This request is taking a while... still {} seconds to go'.format(5 - i)

def get_sample_context():

    long_response = simulate_long_response_with_delay()
    mystring = 'I am a string stored in the context dict'
    context = {'mylist': [1, 2, 3, 4, 5], 'mystring': mystring, 'mylongresponse': long_response}

    return context

def jinja_generate_with_template(template_filename, context):

    template_dir = os.path.dirname(os.path.abspath(__file__)) + '/templates/'

    j2_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
    j2_template = j2_env.get_template(template_filename)
    j2_generator = j2_template.generate(context)
    
    return j2_generator

def run_darkflow():
    options = {
                "model": "./cfg/v1.1/tiny-yolov1.cfg",
                "load": "./bin/tiny-yolo-v1.1.weights",
                "threshold": 0.1,
                "demo": "camera",
            }

    tfnet = TFNet(options)
    return tfnet.camera()