from django.contrib.formtools.preview import FormPreview
from example.joinform import forms

class SomeModelFormPreview(FormPreview):

    
    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        return HttpResponse('HI')

    
        
