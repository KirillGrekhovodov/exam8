from django import forms

from webapp.models import Product, Review
from django.forms import widgets


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "picture"]
        widgets = {"description": widgets.Textarea}


class UserReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "mark"]
        widgets = {"text": widgets.Textarea}


class ModeratorReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "mark", "is_moderated"]
        widgets = {"text": widgets.Textarea}