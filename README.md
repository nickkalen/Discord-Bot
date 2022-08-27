# Discord Integration Project

This is a Container that contains the script movies.py that posts to the Bot channel in our Discord!

## How it works

Movies.py inputs one parameter (a year) and outputs the highest grossing movie of that year, how much money they made, and their movie poster. The magic of this is in the movies.py script, which utilizes a public API called themoviedb (TMDb), whose documentation is linked below:

https://developers.themoviedb.org/3/getting-started/introduction

The script uses the user input to get a year, then parses the json to find movies that were released in that year in descending order of revenue. Then, the movie title, revenue, and poster image are extracted from the json and posted to the discord bot channel by using the discord API with our special discord webhook.

For running the code, I am pretty sure that my TMDb API authentification key should work for the API to run, but if it does not work then you can create an account for free and then follow the steps in the above link to create your own API key. The only reason why I did not consider my TMDb API key as sensitive information is because I made it for free and did not attach my credit card or any other sensitive information to their website. This TMDb API key is in the passwords.py and is accessed in the movies.py file.

However, the discord API key is going to be passed as an environmental variable in our docker run statement, so we do not need to worry about that sensitive information being distributed to the public.

Some limitations of this data is that the gross revenue does not account for inflation, so we need to be careful if we use this data to compare different year's highest revenue movies.

## Setting up the container

First, make sure you have docker on your local machine. You can download the application using this link:
https://docs.docker.com/get-docker/

but to check if it is on your local machine run:
pip3 install docker

After docker is on your local machine, click this link which leads to my dockerhub account image where you can pull the files for my project:
https://hub.docker.com/r/nickkalen/project1

Or to save you time you can simply put this in the terminal:

*docker pull nickkalen/project1*

To run the container after pulling it, run this line with the xxxxx/yyyyyy part of the discord
url https://discord.com/api/webhooks/xxxxxxx/yyyyyyyyy as the environmental variable named MY_PASS. The contents of xxxxx/yyyyy can be found in the general channel of our discord.

*docker run -ti -e* MY_PASS=***xxxxxx/yyyyyyy*** *nickkalen/project1*

Once that line is run, the python script will ask you for a year. If you need help, don't type anything and press enter. If you want to exit the prompt, type exit then press enter.

## Conclusion
Overall I learned a ton from this project. At first starting this project was very overwhelming, but with many trials and errors I now have a much better understanding of how all the pieces (github, docker, python, CLI, and API's) work together. Getting to the point where my code worked and posted on the Discord was very satisfying, and in the end I am happy with my work and with how far I've come in this class.

