from django import forms
from .models import User
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class LoginForm(forms.Form):
    id = forms.CharField(label='Your ID', max_length=30)
    pwd  = forms.CharField(label='Your PW', max_length=30)

    def validate(self):
        print("== LoginForm : ID & PW Validation == ")
        print("ID : ", self.cleaned_data['id'])
        print("PW : ", self.cleaned_data['pwd'])
        print("==================================== ")
        
        user = User.objects.filter(id=self.cleaned_data['id']).first()
        if user == None :
            return False
        
        if user.pwd == self.cleaned_data['pwd'] :
            return True
        else:
            return False
        
        
    

""" 
class UserImg(ModelForm):
    class Meta:
        model = Users
        fields = ["upload_img" , "name",]
def handle_uploaded_file(f):
    with open('uploads/test_files/name.txt','wb+') as destination:
        for chunk in f.chunks(): 
            destination.write(chunk) """