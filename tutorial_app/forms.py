from django import forms
from models import Page, Category, UserProfile
from django.contrib.auth.models import User 

class UserForm(forms.ModelForm):
		password = forms.CharField(widget=forms.PasswordInput())

		class Meta:
				model = User
				fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
		class Meta:
				models = UserProfile 
				fields = ('website', 'picture')

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter a category name!")
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Category
		fields = ('name',)

class PageForm(forms.ModelForm):
	title= forms.CharField(max_length=128, help_text='Please enter a page name!')
	url = forms.URLField(max_length=200, help_text="please enter page URL!")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		
		if url and not url.startswith('http://'):
			url = 'http://'+ url
			cleaned_data['url'] = url 
		return cleaned_data

	class Meta:
		model = Page
		exclude = ('category',)
