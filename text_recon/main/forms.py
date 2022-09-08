from django import forms

LANG_CHOICE = (
    ('rus','rus'),
    ('eng','eng')
)

class ImageForm(forms.Form):
   file_upload = forms.FileField()
   lang = forms.ChoiceField(choices=LANG_CHOICE)
