from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class LoginForm(forms.Form):

	username = forms.CharField(label=_('Username'),
		                       widget=forms.TextInput(attrs={'placeholder': _('Username')}))
	password = forms.CharField(label=_('Password'),
		                       widget=forms.PasswordInput(render_value=False,
	                           attrs={'placeholder':_('Password')}))

	def __init__(self, *args, **kwargs):
	    super(LoginForm, self).__init__(*args, **kwargs)
	    self.helper = FormHelper()
	    self.helper.form_method = 'post'
	    self.helper.add_input(Submit('submit', _('Sign In')))