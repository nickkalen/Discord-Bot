#!/usr/bin/env python3

import passwords
import requests
import json
import os

#get key infomation from text file
api_key = passwords.tmbd_apikey
discord_webhook = os.environ['MY_PASS']

#Make sure the user enters a correct year
while True:
    try:
        year = (input("Please enter a year after 1913: "))
        if year == "":
            #Opens a help menu if the user doesn't type anything
            print("\nThis is a help menu: \n\nPlease enter a valid year from 1913 to 2021 to see your results.\nAn example of a valid year is 1999\nIf you would like to exit at this point, type exit at the cursor below:\n\n")
            continue
        
        #Exits if the user types exit
        elif year == "exit":
            exit()
        else:
            #If the user didn't type exit or "", then this will raise the ValueError
            year = int(year)
            
    #Makes the user retry if they type a string instead of an int
    except ValueError:
        print("You are supposed to enter an integer (no decimals) between 1913 and 2021.")
        continue
    
    #Makes the user retry if they put a year in the future
    if int(year) > 2021:
        print("I know it would be cool to look into the future, but please enter a year between 1913 and 2021.")
        continue
    #Makes the user retry if they put a year too far in the past
    elif year <= 1913:
        print("Whoops you entered a year before 1913. Please try again.")
    else:
        break

#Turn year into a string for future use in url's
year = str(year)

#Get the json where release day=year and revenue is in descending order
response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' +  api_key + '&primary_release_year=' + year + '&sort_by=revenue.desc')
largest_revenue = response.json()

#gets the title of the most revenue movie for the specified year
movie_title = largest_revenue['results'][0]['title']

#gets the ID of the movie with the most revenue
id = largest_revenue['results'][0]['id']
#Uses the ID to get the revenue of the top movie
revenue_json = requests.get('https://api.themoviedb.org/3/movie/'+ str(id) +'?api_key=' + api_key + '&language=en-US')
film_revenue = revenue_json.json()
revenue = film_revenue['revenue']

#Gets the poster path of the top movie
poster = 'http://image.tmdb.org/t/p/w500' + str(film_revenue['poster_path'])

#reformats the revenue in dollar format with commas
revenue_formatted = "${:,}".format(int(revenue))

#This is the data we send over to Discord
data = {
    "content": "The highest grossing movie in " + year + " was " + movie_title + ". It made " + revenue_formatted + "!! " + poster, 
    "username": "Patrick",
    "avatar_url": "https://upload.wikimedia.org/wikipedia/en/thumb/3/33/Patrick_Star.svg/460px-Patrick_Star.svg.png"
}

#This block posts the above data to discord
url = "https://discord.com/api/webhooks/" + discord_webhook
response = requests.post(url, json = data)

