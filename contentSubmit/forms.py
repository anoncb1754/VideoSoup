from django import forms


class SubmitForm(forms.Form):

	choices = (
		('Draft', 'Draft'),
		('Online', 'Online'),
		('Offline', 'Offline'),)

	title = forms.CharField(max_length=255)
	link = forms.URLField(initial='http://')
	labels = forms.CharField(max_length=255)
	status = forms.ChoiceField(choices=choices)
	