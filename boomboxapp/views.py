from django.shortcuts import render
import json
from . import models
from datetime import datetime

# Create your views here.

from django.http import HttpResponse

def create_account(request):
    body = request.body
    
    dct = json.loads(body)
    
    """ TODO dct is a dictionary with keys:
    username, docnumber, password, and birthdate (format 'DD/MM/YYYY')
    1) Assign the birthdate of the dictionary to a separate variable
    2) Split the birthdate by its separator '/'
    3) Assign each component of the split birthdate into new variables,
        casting the day and month (but not year) to integers
    4) For the year component, use list slicing to separate the first
        two digits of the year and the last two into separate variables,
        also casting them to integers
    5) Sum the day + month + first_half_year + second_half_year
    6) Get the modulo of this sum by 16 and return it in the response,
        formatting it into a user-friendly message 
    """

    birthdate = dct['birthdate']
    birthdate = birthdate.split('/')

    day = int(birthdate[0])
    month = int(birthdate[1])
    year = birthdate[2]

    first_half_year = int(year[0:2])
    second_half_year = int(year[2:4])

    cabala_number = (day + month + first_half_year + second_half_year) % 16

    
    return HttpResponse ('Your cabala number is: ' + str(cabala_number))

def save_ratings(request):
    return HttpResponse ('Ratings Saved')
