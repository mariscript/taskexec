from django.forms import ModelForm


class CompanyForm(ModelForm):
    class Meta:
        fields = [
            "name"
        ]
