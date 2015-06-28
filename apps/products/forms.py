from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from .models import Product

MONTHS_CHOICES = {
    1:'jan', 2:'feb', 3:'mar', 4:'apr',
    5:'may', 6:'jun', 7:'jul', 8:'aug',
    9:'sep', 10:'oct', 11:'nov', 12:'dec'
}

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'
		widgets = {
		    'production_date': SelectDateWidget(
		    	months = MONTHS_CHOICES,
		    ),
		    'date_received': SelectDateWidget(
		    	months = MONTHS_CHOICES
		    ),
		    'expiry_date': SelectDateWidget(
		    	months = MONTHS_CHOICES
		    ),
		}
	# qty = forms.CharField(label='Antal')
	# i_type = forms.CharField(label='Enhed')
	# name = forms.CharField(label='Produkt')
	# weight_per_item = forms.CharField(label='weight_per_item')
	# production_date = forms.DateField(label='Production Date')
	# date_rceived = forms.DateField(label='Date recieved')
	# expiry_date = forms.DateField(label='Expiry Date')
	
	def __init__(self, *args, **kwargs):
	    self.helper  = FormHelper()
	    self.helper.layout = Layout(
	    	Fieldset(
	    		'',
	    		'store'
	    	),
	    	Fieldset(
	    		'',
	    		'qty',
	    		'i_type',
	    		'name',
	    		'weight_per_item'
	    	),
	    	Fieldset(
	    		'',
	    		'production_date',
	    		'date_received',
	    		'expiry_date',
	    	),
	    	Fieldset(
	    		'',
	    		'status',
	    		'position',
	    		'description'
	    	),
	    	ButtonHolder(
	    		Submit('submit', 'Submit')
	    	)
	    )
	    super(ProductForm, self).__init__(*args, **kwargs)

