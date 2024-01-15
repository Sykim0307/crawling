from django import forms
from .models import UserModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class SignUpForm(forms.Form):
    username = forms.CharField(label='Your Name', max_length=30)
    password  = forms.CharField(label='Your PW', max_length=30)
    email = forms.CharField(label='Your Email', max_length=30)
    
    def make_user(self):
        try:
            user = User.objects.create_user(self.cleaned_data['username'],self.cleaned_data['email'],self.cleaned_data['password'])
            return user
        except Exception as e:
            print("Sign Up Failed : ", e)
            return -1
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Your ID', max_length=30)
    password  = forms.CharField(label='Your PW', max_length=30)

    def validate(self , request ):
        user = authenticate(request, username=self.cleaned_data['username'], password= self.cleaned_data['password'])
        if user is not None :
            login(request, user)
            return user
        else:
            print("Log in Failed")
            return -1
        
        
        
    

""" 
class UserImg(ModelForm):
    class Meta:
        model = Users
        fields = ["upload_img" , "name",]
def handle_uploaded_file(f):
    with open('uploads/test_files/name.txt','wb+') as destination:
        for chunk in f.chunks(): 
            destination.write(chunk) """