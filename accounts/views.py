from django.shortcuts import render, redirect
from .models import CustomUser, UserData, State, UserDocuments
from django.contrib import messages
import random
from twilio.rest import Client
from django.contrib.auth import authenticate, login, logout
from main.decorators import allowed_group

from .thread import SendOtpThread

# Create your views here.

# def send_otp(otp, phone):
#     account_sid = 'AC8b5ead76bcce5709a6edddf570cbe9d4'
#     auth_token = 'a32f6ddb034bcb9777aecf62ecfc026b'
#     client = Client(account_sid, auth_token)

#     client.messages.create(
#         body=f'{otp} is your one time password(OTP) for phone verification by Grofusion.com',
#         from_='+13366523298',
#         to= '+91' + phone)
    
#     return None

def register_handler(request):
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        type = request.POST.get('select')

        if pass1 == pass2:
            ph_len = len(phone)

            if CustomUser.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already registered')
                return redirect('index')

            elif ph_len > 13:
                messages.warning(request, 'Enter a valid phone number')
                return redirect('index')

            elif ph_len < 13:
                if not phone.isdigit():
                    if phone[0] != '+':
                        messages.warning(request, 'Enter a valid phone number')
                        return redirect('index')

            request.session['name'] = name
            request.session['email'] = email
            request.session['phone'] = phone
            request.session['pass'] = pass1
            request.session['type'] = type

            otp = str(random.randint(10000, 99999))
            request.session['otp'] = otp
            
            SendOtpThread(otp, phone).start()

            return redirect('otp')
            
        else:
            messages.error(request, 'Passwords does not match')
            return redirect('index')
       
    return redirect('index')

def otp_handler(request):

    phone = request.session['phone']
    name = request.session['name']
    email = request.session['email']
    pass1 = request.session['pass']
    type = request.session['type']

    if request.method == "POST":
        otp = request.POST.get('otp')
        if otp == request.session['otp']:
            user = CustomUser.objects.create_user(email, phone, name, type, pass1)
            user.save()
            user = authenticate(username=email, password=pass1)
            if user is not None:
                login(request, user)

            messages.success(request, 'Your account has been created successfully.')
            return redirect('dashboard')

        else:
            messages.error(request, 'Wrong Otp.')
            return redirect('index')

    context = {'mobile': phone}
    return render(request, 'main/otp.html', context)

def login_handler(request):

    if request.method == 'POST':
        username = request.POST.get('loginemail')
        password = request.POST.get('loginpass')
        type = request.POST.get('loginselect')

        print(username)
        print(password)
        print(type)

        if CustomUser.objects.filter(email=username, type=type).exists():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('dashboard')

            else:
                messages.error(request, 'Wrong Email/Password')

        else:
            messages.warning(request, 'User not registered')

    return redirect('index')

def logout_handler(request):
    if request.user.is_authenticated:
        messages.success(request, f'<strong>{request.user.name}</strong> logged out successfully')
        logout(request)

    return redirect('index')

@allowed_group('Seller')
def update_profile_seller(request):

    user = CustomUser.objects.get(email=request.user.email)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
        npass = request.POST.get('npass')
        cpass = request.POST.get('cpass')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')

        if name != user.name:
            user.name = name
            user.save()

        if email != user.email:
            user.email = email
            user.save()

        if phone != user.phone:
            user.phone = phone
            user.save()

        if npass != '': 
            if npass == cpass:
                user.set_password(npass)
            else:
                messages.error(request, 'Passwords does not match')

        if UserData.objects.filter(user=user).exists():
            data = UserData.objects.get(user=user)
            data.address = address
            data.state = State.objects.get(value=state)
            data.city = city
            data.pincode = pincode
            data.save()
            messages.success(request, 'Profile Updated successfully!')

        else:
            UserData(
                user=user,
                address = address,
                state = State.objects.get(value=state),
                city = city,
                pincode = pincode
            ).save()
            messages.success(request, 'Profile Updated successfully!')
        
        return redirect('dashboard')

    context = {}
    if UserData.objects.filter(user=user).exists():
        data = UserData.objects.get(user=user)
        context = {'address': data.address, 'state': data.state.value, 'city': data.city, 'pincode': data.pincode}

    return render(request, 'main/update-profile-seller.html', context)

@allowed_group('Seller')
def upload_documents_seller(request):

    user = CustomUser.objects.get(email=request.user.email)
    if request.method == 'POST':
        aadhar = request.FILES['image']
        check = request.FILES['image2']

        if UserDocuments.objects.filter(user=user).exists():
            user.aadhar_card = aadhar
            user.cancelled_check = check

            messages.success(request, 'Documents uploaded successfully.')

        else:
            UserDocuments(
                user=user,
                aadhar_card = aadhar,
                cancelled_check = check
            ).save()

            messages.success(request, 'Documents uploaded successfully.')
    context = {}
    if UserDocuments.objects.filter(user=user).exists():
        data = UserDocuments.objects.get(user=user)
        context = {'aadhar': data.aadhar_card, 'check': data.cancelled_check}

    return render(request, 'main/upload-documents-seller.html', context)


@allowed_group('Buyer')
def update_profile_buyer(request):

    user = CustomUser.objects.get(email=request.user.email)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
        npass = request.POST.get('npass')
        cpass = request.POST.get('cpass')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')

        if name != user.name:
            user.name = name
            user.save()

        if email != user.email:
            user.email = email
            user.save()

        if phone != user.phone:
            user.phone = phone
            user.save()

        if npass != '': 
            if npass == cpass:
                user.set_password(npass)
            else:
                messages.warning(request, 'Passwords does not match')

        if UserData.objects.filter(user=user).exists():
            data = UserData.objects.get(user=user)
            data.address = address
            data.state = State.objects.get(value=state)
            data.city = city
            data.pincode = pincode
            data.save()
            messages.success(request, 'Profile Updated successfully.')

        else:
            UserData(
                user=user,
                address = address,
                state = State.objects.get(value=state),
                city = city,
                pincode = pincode
            ).save()
            messages.success(request, 'Profile Updated successfully.')
        
        return redirect('dashboard')

    context = {}
    if UserData.objects.filter(user=user).exists():
        data = UserData.objects.get(user=user)
        context = {'address': data.address, 'state': data.state.value, 'city': data.city, 'pincode': data.pincode}

    return render(request, 'main/update-profile-buyer.html', context)