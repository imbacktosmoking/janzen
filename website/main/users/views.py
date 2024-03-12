from django.shortcuts import render, redirect
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.views.generic.base import View
from . models import Student
from django.contrib.auth import login







class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(
                user=user,
                gender=form.cleaned_data['gender'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
            )
            login(request, user)
            return redirect('homepage')
        return render(request, self.template_name, {'form': form}) 



