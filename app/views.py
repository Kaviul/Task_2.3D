import os
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import Student
from django.views.decorators.csrf import csrf_protect
from django import forms
from .forms import MyForm


def my_form(request):
    form = MyForm()
    context = {'form': form}
    if request.method == 'POST':
        print(request.POST)
        form = MyForm(request.POST)

        if form.is_valid():

            givenName = form.cleaned_data['givenName']
            familyName = form.cleaned_data['familyName']
            sex = form.cleaned_data['sex']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']

            file_path = os.path.join(
                'C:/Users/Kaviul/Desktop/Task_2.1D', 'form_data.txt')
            with open(file_path, 'a') as f:
                f.write(
                    f'Given_Name: {givenName}\nFamily_Name: {familyName}\nSex: {sex}\nEmail: {email}\nAddress: {address}\n\n')
                return render(request, 'std_add.html')

        else:

            form = MyForm()
            return render(request, 'std_add.html', context)

    return render(request, 'std_add.html', context)
