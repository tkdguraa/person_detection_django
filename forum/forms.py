from django import forms

class changeform(forms.Form):
    Oldpassword = forms.CharField(label = 'Oldpassword')
    Newpassword = forms.CharField(label = 'Newpassword')
    Confirmpass = forms.CharField(label = 'Confirmpass')

class userform(forms.Form):
    Username = forms.CharField(label = 'Username')
    Password = forms.CharField(label = 'Password')
    Confirmpass = forms.CharField(label = 'Confirmpass')

class warningform(forms.Form):
    Tphase1 = forms.CharField(label = 'Tphase1')
    Tphase2 = forms.CharField(label = 'Tphase2')
    Pphase1 = forms.CharField(label = 'Pphase1')
    Pphase2 = forms.CharField(label = 'Pphase2')
    peoplenumber = forms.CharField(label = 'peoplenumber')                            
    staytime = forms.CharField(label = 'staytime')