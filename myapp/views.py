from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, ContactForm
from .models import BloodBank




# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')  # Make sure you have this template

def blood_bank_view(request):
    return render(request, 'stock_availability.html')

from django.shortcuts import render
from .models import State, District 

def blood_stock(request):
    states = State.objects.all()
    districts = District.objects.all()
    blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    results = None

    if request.GET:
        state_id = request.GET.get('state')
        district_id = request.GET.get('district')
        blood_group = request.GET.get('blood_group')
        component = request.GET.get('component')

        

    return render(request, 'blood_stock.html', {
        'states': states,
        'districts': districts,
        'blood_groups': blood_groups,
        'results': results,
    })

def blood_banks(request):
    if request.method == "GET":
        state = request.GET.get("state")
        district = request.GET.get("district")
        search_query = request.GET.get("search", "")

        # Filter logic
        blood_banks = BloodBank.objects.all()
        if state:
            blood_banks = blood_banks.filter(address__icontains=state)
        if district:
            blood_banks = blood_banks.filter(address__icontains=district)
        if search_query:
            blood_banks = blood_banks.filter(name__icontains=search_query)

        return render(request, "blood bank directory.html", {"blood_banks":blood_banks})
    

def camp_schedule(request):
    return render(request, 'donation_camps.html')


from .forms import CampRegistrationForm
from .models import CampRegistration


def camp_registration(request):
    if request.method == 'POST':
        form = CampRegistrationForm(request.POST)
        if form.is_valid():
            camp_registration = CampRegistration(
                organization_type=form.cleaned_data['organization_type'],
                organization_name=form.cleaned_data['organization_name'],
                organizer_name=form.cleaned_data['organizer_name'],
                organizer_mobile=form.cleaned_data['organizer_mobile'],
                organizer_email=form.cleaned_data['organizer_email'],
                co_organizer_name=form.cleaned_data['co_organizer_name'],
                co_organizer_mobile=form.cleaned_data['co_organizer_mobile'],
                camp_name=form.cleaned_data['camp_name'],
                camp_address=form.cleaned_data['camp_address'],
                state=form.cleaned_data['state'],
                district=form.cleaned_data['district'],
                city_name=form.cleaned_data['city_name'],
                bloodbank=form.cleaned_data['bloodbank'],
                camp_propose_date=form.cleaned_data['camp_propose_date'],
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude'],
                estimated_participants=form.cleaned_data['estimated_participants']
            )
            camp_registration.save()
            print(form.cleaned_data)
            return redirect('success')
    else:
        form = CampRegistrationForm()

    return render(request, 'camp_registration.html', {'form': form})

from django.http import JsonResponse
from django.shortcuts import render
from .forms import CampRegistrationForm

# Dictionary mapping states to their districts (for simplicity, based on Telangana)
DISTRICTS_BY_STATE = {
    'TG': [
        
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
             
        
        # Add other districts as needed...
    ],
    'AP': [
       
    ('East Godavari', 'East Godavari'),
    ('Guntur', 'Guntur'),
    ('Krishna', 'Krishna'),
    ('Kurnool', 'Kurnool'),
    ('Prakasam', 'Prakasam'),
    ('Srikakulam', 'Srikakulam'),
    ('Visakhapatnam', 'Visakhapatnam'),
    ('Vizianagaram', 'Vizianagaram'),
    ('West Godavari', 'West Godavari'),
    ('YSR Kadapa', 'YSR Kadapa'),
    ('Nellore', 'Nellore'),
    ('West Godavari', 'West Godavari'),
    ('Tirupati', 'Tirupati'),
    ('Sri Potti Sriramulu Nellore', 'Sri Potti Sriramulu Nellore')
        
    ],
    # Add other states here...
}

def get_districts(request):
    state = request.GET.get('state')
    districts = DISTRICTS_BY_STATE.get(state, [])
    return JsonResponse({'districts': districts})

def camp_registration(request):
    form = CampRegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Handle form submission here
        pass

    return render(request, 'camp_registration.html', {'form': form})

def success(request):
    return render(request, 'success.html') 




