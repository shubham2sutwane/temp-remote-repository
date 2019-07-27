from django import forms


class Contactform(forms.Form):
    name= forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Name Here',
                'class': 'form-control'
            }
        )
    )
    location= forms.CharField(
        label="Enter Your Location",
        widget= forms.TextInput(
            attrs= {
                'placeholder': 'Your Location Here',
                'class': 'form-control'
            }
        )
    )
    salary = forms.IntegerField(
        label="Enter Your Salary",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Your Salary Here',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Your Email-ID Here',
                'class': 'form-control'
            }
        )
    )


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Your Name here',
                'class': 'form-control'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'placeholder' : 'Your Rating here',
                'class': 'form-control'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'placeholder' : 'Your Feedback here',
                'class': 'form-control'
            }
        )
    )