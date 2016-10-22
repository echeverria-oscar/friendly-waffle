from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .models import Trip
import datetime


# Create your views here.
def index(request):

    return render(request, 'belt_exam/index.html')

def register(request):
    if request.method == "POST":
       form_errors = User.objects.validate(request.POST)

    if len(form_errors) > 0:
       for error in form_errors:
           messages.error(request, error)
    else:
        User.objects.register(request.POST)
        messages.success(request, "You have successfully registered! Please login to continue")

    return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.objects.login(request.POST)
        if not user:
            messages.error(request, "Not login credentials!")
        else:
           request.session['logged_user'] = user.id
           return redirect('/travels')

def logout(request):
    if 'logged_user' in request.session:
        request.session.pop('logged_user')
    return redirect('/')


def travels(request):
    if 'logged_user' not in request.session:
        return redirect('/')

    trip = Trip.objects.all().order_by('created_at')
    usertrip = Trip.objects.filter(user_id = request.session['logged_user'])
    context = {
        'user' : User.objects.get(id = request.session['logged_user']),
        'trips' : trip,
        'usertrips': usertrip
    }
    return render(request, 'belt_exam/travels.html', context)

def addplan(request):

    return render(request, 'belt_exam/addplan.html')

def process_plan(request):
    user_id = request.session['logged_user']
    if request.method == "POST":
        form_errors = Trip.objects.maketrip(request.POST)

        if len(form_errors) > 0:
            for error in form_errors:
                messages.error(request, error)
                return redirect('/addplan')
        else:
            Trip.objects.create(destination = request.POST['destination'], description = request.POST['description'], travel_from = request.POST['travel_from'], travel_to = request.POST['travel_to'], user_id =user_id )
            messages.success(request, "You have successfully registered! Please login to continue")


        return redirect('/travels')

def locations(request, id):
    trip = Trip.objects.get(id=id)

    context = {
        'trip' : trip
    }

    return render(request, 'belt_exam/location.html', context)

def join(request, id):

    if request.method == "GET":



        return redirect('/locations')
