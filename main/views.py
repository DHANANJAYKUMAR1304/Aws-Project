from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django import forms

# Create your views here.
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name','email','message','document',)
def home(request):

    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = DocumentForm()
    return render(request,'contactus.html',{'form':form})
