from django import forms

class ImageForm(forms.Form):
    file_upload = forms.FileField()