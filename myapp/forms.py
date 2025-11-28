from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    blood_type = forms.ChoiceField(choices=[('A+', 'A+'), ('A-', 'A-'), ...])

class ContactForm(forms.Form):
    contact_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


from django import forms

class CampRegistrationForm(forms.Form):
    ORGANIZATION_TYPE_CHOICES = [
        ('ngo', 'NGO'),
        ('hospital', 'Hospital'),
        ('other', 'Other'),
    ]

    STATE_CHOICES = [
    ('', 'Select State'),
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CT', 'Chhattisgarh'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JK', 'Jammu & Kashmir'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OD', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TG', 'Telangana'),
    ('UP', 'Uttar Pradesh'),
    ('UK', 'Uttarakhand'),
    ('WB', 'West Bengal'),
    ('AN', 'Andaman and Nicobar Islands'),
    ('CH', 'Chandigarh'),
    ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('DD', 'Lakshadweep'),
    ('LD', 'Delhi'),
    ('PY', 'Puducherry')
]


    DISTRICT_CHOICES = [
    ('', 'Select District'),
    ('Adilabad', 'Adilabad'),
    ('Bhadradri Kothagudem', 'Bhadradri Kothagudem'),
    ('Hyderabad', 'Hyderabad'),
    ('Jagtial', 'Jagtial'),
    ('Jangaon', 'Jangaon'),
    ('Jayashankar Bhupalpally', 'Jayashankar Bhupalpally'),
    ('Jogulamba Gadwal', 'Jogulamba Gadwal'),
    ('Kamareddy', 'Kamareddy'),
    ('Karimnagar', 'Karimnagar'),
    ('Khammam', 'Khammam'),
    ('Komaram Bheem Asifabad', 'Komaram Bheem Asifabad'),
    ('Mahabubabad', 'Mahabubabad'),
    ('Mahabubnagar', 'Mahabubnagar'),
    ('Mancherial', 'Mancherial'),
    ('Medak', 'Medak'),
    ('Medchal-Malkajgiri', 'Medchal-Malkajgiri'),
    ('Mulugu', 'Mulugu'),
    ('Nagar Kurnool', 'Nagar Kurnool'),
    ('Nirmal', 'Nirmal'),
    ('Nizamabad', 'Nizamabad'),
    ('Peddapalli', 'Peddapalli'),
    ('Rajanna Sircilla', 'Rajanna Sircilla'),
    ('Rangareddy', 'Rangareddy'),
    ('Sangareddy', 'Sangareddy'),
    ('Siddipet', 'Siddipet'),
    ('Suryapet', 'Suryapet'),
    ('Vikarabad', 'Vikarabad'),
    ('Wanaparthy', 'Wanaparthy'),
    ('Warangal', 'Warangal'),
    ('Warangal Rural', 'Warangal Rural'),
    ('Yadadri Bhuvanagiri', 'Yadadri Bhuvanagiri')
]


    BLOODBANK_CHOICES = [
        ('', 'Select BloodBank'),
        ('bb1', 'BloodBank 1'),
        ('bb2', 'BloodBank 2'),
    ]

    organization_type = forms.ChoiceField(choices=ORGANIZATION_TYPE_CHOICES, required=True)
    organization_name = forms.CharField(max_length=100, required=True)
    organizer_name = forms.CharField(max_length=100, required=True)
    organizer_mobile = forms.CharField(max_length=15, required=True)
    organizer_email = forms.EmailField(required=False)
    co_organizer_name = forms.CharField(max_length=100, required=False)
    co_organizer_mobile = forms.CharField(max_length=15, required=False)
    camp_name = forms.CharField(max_length=100, required=True)
    camp_address = forms.CharField(widget=forms.Textarea, required=True)
    state = forms.ChoiceField(choices=STATE_CHOICES, required=True)
    district = forms.ChoiceField(choices=DISTRICT_CHOICES, required=True)
    city_name = forms.CharField(max_length=100, required=True)
    bloodbank = forms.ChoiceField(choices=BLOODBANK_CHOICES, required=True)
    camp_propose_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=True)
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=True)
    latitude = forms.CharField(max_length=50, required=False)
    longitude = forms.CharField(max_length=50, required=False)
    estimated_participants = forms.IntegerField(required=True)
