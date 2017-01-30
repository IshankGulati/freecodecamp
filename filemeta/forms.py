from django import forms


class FileForm(forms.Form):
    fileupload = forms.FileField()