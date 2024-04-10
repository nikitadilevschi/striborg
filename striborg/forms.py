from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = user.email
        user.is_active = False  # Set is_active to False by default
        user.save()
        return user