from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from .forms import LoginForm

def signin(request, form_class=None,
           template_name = 'registration/signin.html',
           redirect_field_name = REDIRECT_FIELD_NAME,
           extra_context = None):
	
	form = form_class
	
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			username, password = (form.cleaned_data['username'],
				                  form.cleaned_data['password'])


			user = authenticate(username = username,
				                password = password)

			if user.is_active:
				login(request, user)
				return redirect(reverse('index'))
			else:
				return redirect(reverse('user_disabled'))
	
	if extra_context is None:
		extra_context = {}
	context = RequestContext(request)
	for key, value in extra_context.items():
		context[key] = callable(value) and value() or value
		
	return render_to_response(template_name,
	                          {'form': form,
	                           'next': request.REQUEST.get(redirect_field_name)},
	                           context_instance=context)

def signout(request):
	logout(request)
	return HttpResponseRedirect("/")
