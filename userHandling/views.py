# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf


def signup(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':

		signup_form = UserCreationForm(request.POST)
		if signup_form.is_valid():
			new_user = signup_form.save()
			return HttpResponseRedirect("/submit")
	else:
		signup_form = UserCreationForm()
	return render(request, "signup.html", {'form': signup_form})

