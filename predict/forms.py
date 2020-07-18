from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import ModelForm
from predict.models import PredictModel

# Gender=(("f","Female"),("m","Male"))

# Age=(("15","15"),("16","16"),("17","17"),("18","18"),("19","19"),("20","20"),("21","21"),("22","22"))

# failures=(("0","None"),("1","1"),("2","2"),("3","3"),("4","More than 4"))

# Goout=(("1","Very Low"),("2","Low"),("3","Average"),("4","High"),("5","Very High"))

# Dalc=(("1","Very Low"),("2","Low"),("3","Average"),("4","High"),("5","Very High"))

# Higher=(("y","Yes"),("n","No"))

# famrel=(("1","Very bad"),("2","Bad"),("3","Neutral"),("4","Good"),("5","Very Good"))


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class MyPredictForm(ModelForm):
	class Meta:
		model = PredictModel
		fields = ['student_id','first_name', 'last_name', 'gender','age','failures','pstatus','dalc','higher','famrel','G1','G2']