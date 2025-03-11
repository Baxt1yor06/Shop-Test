from django import forms
from product.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].help_text = 'Bu yerga ismingizni kiriting'
        print(self)



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'gender', 'message']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailingizni kiriting'}),
            "number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingizni kiriting'}),
            "gender": forms.Select(attrs={'class': 'form-control'}),
            "message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabaringizni kiriting'}),
        }
