from django import forms
from .models import Business


# creating a form
class BusinessModelForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Business

		# specify fields to be used
		fields = '__all__'
