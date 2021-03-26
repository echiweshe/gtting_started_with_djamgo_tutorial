#forms.py
from django import forms
from myapp.models import Member
 
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('username', 'firstname', 'lastname', 'email', 'bio',)
