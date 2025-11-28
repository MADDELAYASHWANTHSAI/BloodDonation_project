from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
from django.db import models

class BloodStock(models.Model):
    blood_type = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.blood_type} - {self.quantity} units"
    from django.db import models

class BloodBank(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    category = models.CharField(max_length=100)
    distance = models.FloatField()
    bank_type = models.CharField(max_length=100)

    def _str_(self):
        return self.name



from django.db import models

class CampRegistration(models.Model):
    ORGANIZATION_TYPE_CHOICES = [
        ('ngo', 'NGO'),
        ('hospital', 'Hospital'),
        ('other', 'Other'),
    ]
    
    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        # add other states here
    ]
    
    DISTRICT_CHOICES = [
        ('Anantapur', 'Anantapur'),
        ('Chittoor', 'Chittoor'),
        # add other districts here
    ]
    
    BLOODBANK_CHOICES = [
        ('bb1', 'BloodBank 1'),
        ('bb2', 'BloodBank 2'),
    ]
    
    organization_type = models.CharField(max_length=20, choices=ORGANIZATION_TYPE_CHOICES)
    organization_name = models.CharField(max_length=100)
    organizer_name = models.CharField(max_length=100)
    organizer_mobile = models.CharField(max_length=15)
    organizer_email = models.EmailField(blank=True)
    co_organizer_name = models.CharField(max_length=100, blank=True)
    co_organizer_mobile = models.CharField(max_length=15, blank=True)
    camp_name = models.CharField(max_length=100)
    camp_address = models.TextField()
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES)
    city_name = models.CharField(max_length=100)
    bloodbank = models.CharField(max_length=20, choices=BLOODBANK_CHOICES)
    camp_propose_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    latitude = models.CharField(max_length=50, blank=True)
    longitude = models.CharField(max_length=50, blank=True)
    estimated_participants = models.IntegerField()

    def __str__(self):
        return self.camp_name
