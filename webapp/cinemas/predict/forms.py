from django import forms


class UploadFileForm(forms.Form):

    csv_file = forms.FileField(label='Select file for import')
