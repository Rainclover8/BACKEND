from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User



class changePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields= ['new_password1','new_password2']

    def __init__(self, *args, **kwargs):
            super(changePasswordForm, self).__init__(*args, **kwargs)

            for fieldname in ['new_password1', 'new_password2']:
                self.fields[fieldname].help_text = None




class registerForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
            super(registerForm, self).__init__(*args, **kwargs)

            for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None