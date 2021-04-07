from django.forms import ModelForm
from .models import  Product



class ProjectForm(ModelForm):
	
	class Meta:        
		model = Product
		# fields= "__all__"
		exclude = ('owner',)
