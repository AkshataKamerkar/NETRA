import json

#import cv2
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import FormView
from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from .forms import ContactForm
from .models import Contact
from .utils import send_email_to_client
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
import logging
from django.http import JsonResponse, HttpResponseRedirect, request
from django.views import View
import json
#import pandas as pd
#from ultralytics import YOLO

'''
    Total 4 Routes 
        - LandingPage      : Nav, MainVideo/ MainModel, Services, Features, Contact Form, Testimonials, Footer 
        - About Page       : Nav, About Content, Footer 
        - LogInSignUp Page : AllAuth
        - Dashboard Page   : Main page where the insights will be presented

    Total 1 Forms 
        - Contact Us : On LandingPage  
         
'''



class LandingPage(FormView):
    template_name = 'landingPage.html'
    form_class = ContactForm
    success_url = '/'  # Redirect URL after successful form submission

    def form_valid(self, form):
        form.save()  # This saves the form data to the database using the model

        # To send the contact mail
        ls_email = []
        email = form.cleaned_data['email']
        fname = form.cleaned_data['fname']
        # To get the latest mail
        ls_email.append(email)

        # Calling the actual function
        send_email_to_client(ls_email, fname)

        # To avoid sending mail to the previous users
        ls_email.clear()

        messages.info(self.request, 'Your message has been successfully submitted !! ')

        return super().form_valid(form)


# AboutUs is a TemplateView since we just hv to render a simple template and dont have to perform form based or data retrival frm the models operations
# Creating the About Us Page
class AboutUs(TemplateView):
    template_name = 'about.html'


class Dashboard(TemplateView):
    template_name = 'dashboard.html'




