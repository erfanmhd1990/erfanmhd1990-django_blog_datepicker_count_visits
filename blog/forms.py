from django import forms
from blog.models import BlogPost
from bootstrap_datepicker_plus import  DateTimePickerInput
from django_flatpickr.widgets import DateTimePickerInput
from django import forms

class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image','pub_date']
        def get_form(self):
            form = super().get_form()
            form.fields['pub_date'].widget = DateTimePickerInput()
            return form  

class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image','pub_date']
        def get_form(self):
            form = super().get_form()
            form.fields['pub_date'].widget = DateTimePickerInput()
            return form 
        
    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']
        blog_post.pub_date = self.cleaned_data['pub_date']
        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']
        if commit:
            blog_post.save()
        return blog_post