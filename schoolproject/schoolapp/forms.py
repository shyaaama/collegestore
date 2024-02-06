from django import forms

from .models import Department,Course,Person
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
# forms.py
from django import forms
from .models import Department, Course
class PersonCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=124)
    dob = forms.DateField()
    age = forms.IntegerField()
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).all()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')

    PURPOSE_CHOICES = [
        ('enquiry', 'For Enquiry'),
        ('order', 'Place Order'),
        ('return', 'Return'),
    ]

    MATERIALS_PROVIDE_CHOICES = [
        ('notebook', 'Notebook'),
        ('pen', 'Pen'),
        ('exam_papers', 'Exam Papers'),
    ]

   
    
   
    gender = forms.CharField(max_length=10)
    phone_number = forms.CharField(max_length=15)
    mail_id = forms.EmailField()
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=False)
    address = forms.CharField(max_length=255)
    purpose = forms.CharField(max_length=20, widget=forms.Select(choices=PURPOSE_CHOICES))
    materials_provide = forms.MultipleChoiceField(
        choices=MATERIALS_PROVIDE_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )



# yourapp/forms.py









 