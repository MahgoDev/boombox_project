from django.shortcuts import render
import json
from . import models
from datetime import datetime
from django.db.utils import IntegrityError

# Create your views here.

from django.http import HttpResponse

def _get_rating(id_rating_item):
    return list(id_rating_item.values())[0]

""" TODO
To finalize the project, we must save the data passed to the endpoints
    in the database. This is done using the lines below for each entity.

# Account
account = models.Account(username=, docnumber=, password=, creation_date=datetime.now())
account.save()
id = account.id

# Album
album = models.Album(album_name=, release_date=, creation_date=datetime.now())
album.save()
id = album.id

# Rating
album = models.Album.objects.get(name=)
account = models.Account.objects.get(username=)
rating = models.Rating(album=album, account=account, rating=, creation_date=)
rating.save()
id = rating.id

Define functions that receive arguments for each entity's fields and fill their
    usage in the snippets above, returning the saved object's id.
    Call these functions in the endpoints passing the request data, printing
    the id's returned by the function call.

For the Account endpoint, try sending two requests with the same document number.
    What happened? Why?
    The response is a raw exception and is very unfriendly for the user to
    understand. So, use try-except to catch the thrown Exception and handle it by
    returning an error code 500 and with a message formatted to explain the error
    to the user.

For the Rating endpoint, try sending two requests with the same account and album.
    Then, try sending an account that has not been added, and then repeat for an album.
    What happened in each case? Why?
    Again, use try-except to catch each Exception type separately and handle them by
    returning the error code 500 and with messages formatted to explain the errors
    to the user.
"""

def _create_account(user, doc, passw):
    account = models.Account(username=user, docnumber=doc, password=passw, creation_date=datetime.now())
    account.save()

    id = account.id
    return id

def _album_id(name, release):
    album = models.Album(album_name=name, release_date=release, creation_date=datetime.now())
    album.save()

    id=album.id
    return id

def _album_ratings(disco, user, rate):
    album = models.Album.objects.get(name=disco)
    account = models.Account.objects.get(username=user)

    rating = models.Rating(album=album, account=account, rating=rate, creation_date=datetime.now())
    rating.save()

    id = rating.id
    return id



def create_account(request):

    """
    Request body example:
    {
        "username": "bbbertucci",
        "docnumer": "12345678910",
        "password": "password123"
    }
    """

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

    try:
        id = _create_account(dct['username'], dct['docnumber'], dct['password'])
    except IntegrityError as duplicated_doc:
        return HttpResponse (f'The Doc Number has been used, try another', status = 500 )


    print(f'Your ID User is: {id}')



    return HttpResponse ('Your cabala number is: ' + str(cabala_number))

def add_albums(request):
    """
    Example:
    {
         "content": [
            {"Lover": "2019-08-23"},
            {"Reputation": "2017-11-10"}
        ]
    }
    """

    body = request.body
    
    dct = json.loads(body)

    """ TODO dct is a dictionary with key content,
    which is a list of dictionaries, all of which have
    one key representing the album name, and
    one value representing the album's release date (format YYYY-MM-DD)

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

    dct['my_favorite_album']='Red'
    dct['my_fave_album_release_date']='2012-10-22'

    print(dct['my_favorite_album'], dct['my_fave_album_release_date'])

   
    content = dct['content']
    names = [list(item.keys())[0] for item in content]
    dates = [list(item.values())[0] for item in content]

    print(names[0].lower())
    print(names[1].upper())

    names[0] = 'YOU WERE HACKED!!!!!!!!!'
    names.append('brat_by_charlie_xcx')
    dates.append('2024-06-07')
    print(len(names))

    indice_names = len(names) //2
    indice_dates = len(dates) //2

    names.insert(indice_names,'bitch')
    dates.insert(indice_dates,'1995-10-04')

    print(names)
    print(dates)





    return HttpResponse ('')

def add_ratings(request):
    """
    Example:
    {
        "username": "bbbertucci",
        "content": [
            {"Lover": 9.5},
            {"Reputation": 8.4}
        ]
    }
    """

    body = request.body
    
    dct = json.loads(body)

    """ TODO dct is a dictionary with keys username and content
    content is a list of dictionaries with only one key-value pair,
    where the key is the album name and the value is its rating

    1) Split the "content" dictionary into two lists,
        one only with names and the other with ratings
        Do this using a for loop iterating on a range from 0
        to the list's size

    2) Create a dictionary, initially with this format:
        {
            "Bad": 0,
            "Good": 0,
            "Excellent": 0
        }
        Iterate over the rating list putting it in a for loop.
        Inside it, use if-elif-else to assign a rating range in which:
            [8 - 10]: Excellent
            [6 - 8): Average
            [0, 6): Bad
        Update the dictionary, incrementing the value of the rating range
        found
    3) Create an empty list called top_ratings and
        a counter i, initially zero
    4) Using the sort method with key as the function _get_rating,
        sort the original "content" list by rating in descending order
    5) Start a while loop with condition where the length of top_ratings is
        smaller than half of the ratings list and the rating for the current
        value of the counter is larger than 5
    6) Add the rating for the current value of the counter to the top_ratings list
    7) To finish this loop, increment i, check if it is smaller than the rating
        list's length to avoid errors
        on the next iteration (it it's not, break the loop)
    9) Format the response with the following information:
        - Number of ratings in each rating range    
        - Top ratings
        - Smallest album in the top ratings

    """
    content = dct['content']
    album_name=[]
    album_rating=[]

    for i in range(0,len(content)):
        item = content[i]
        album_name.append(list(item.keys())[0])
        album_rating.append(list(item.values())[0])

    stars ={
            "Flop": 0,
            "Good": 0,
            "Excellent": 0
        }

    for av in album_rating:
       
        if av >=8:
            star = 'Excellent'
        elif av >=6:
            star = 'Good'
        else:
            star = 'Flop'
        
        stars[star] = stars[star] + 1
    
    top_ratings = []
    counter_i = 0

    content.sort(reverse=True, key=_get_rating)
    album_rating_sorted=[]

    for i in range(0,len(content)):
        item = content[i]
        album_rating_sorted.append(list(item.values())[0])
    
    mid_list = len(album_rating_sorted)//2
    
    while counter_i <= mid_list and album_rating_sorted[counter_i] >= 5:
        top_ratings.append(album_rating_sorted[counter_i])
        counter_i += 1
        if counter_i >= len(album_rating_sorted):
            break
    
    flopest_album = content[counter_i - 1]

    response = f"The album scores is {stars}!!!, \n The grestest albums is {top_ratings} \n and the flopest album is {flopest_album}!!!"

    return HttpResponse(response)
