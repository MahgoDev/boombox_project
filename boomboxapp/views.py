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

def add_albums(request):
    body = request.body
    
    dct = json.loads(body)

    """ TODO dct is a dictionary with key content,
    which is a list of dictionaries, all of which have
    one key representing the album name, and
    one value representing the album's release date (format YYYY-MM-DD)
    Example:
    {
         "content": [
            {"Lover": "2019-08-23"},
            {"Reputation": "2017-11-10"}
        ]
    }

    1) Update the dictionary with a new entry, with a
        album name and release date that you (the server owner)
        really enjoy
    2) Print the date of the album you just added to the
        dictionary using the dictionary and the album name key,
        then remove it from the dictionary using the key again
    3) Using list comprehension, convert the list of
        dictionaries into two separate lists: one
        only with names and one only with release dates.
        Hint: the method .items() on a dictionary converts
        it into a list of tuples
    4) Print the first album name converted to lowercase,
        and the second one converted to uppercase
    5) Replace the first album name with 'YOU WERE HACKED'
    6) Append a random name on the name list and a random date
        on the date list. Print the new list length.
    7) Insert a random name on the name list and a random date
        on the date list, the insert position must be the integer
        part of half of the lists' lengths. Print the new list length.
    8) Remove the items you've just appended and inserted;
        the replaced item unfortunately is corrupted data.
        Print the new list length.
    9) Copy the dates to a new list, then sort and print it;
        are the dates in proper chronological order?
        Would this happen in any date format?
    10) Format the response with fun facts about the consumed data:
    Get the years of the date list into a new list by using
        list comprehension together with splitting the date string
        by its separator (-) and getting the last item of the
        resulting list, then also inform:
            - The oldest year
            - The newest year
            - The sum of all years (kind of useless but whatever)
    """

    return HttpResponse ('')
