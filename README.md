This is a Container that contains the script movies.py that posts to the Bot channel in our Discord!

## How it works

movies.py inputs one parameter (a year) and outputs the highest grossing movie of that year, how much money they made, and their movie poster.

Here is a link to the API documentation I used for the movies:
https://developers.themoviedb.org/3/getting-started/introduction

For running the code, I am pretty sure that my API authentification key should work for the API to run, but if it does not work then you can create an account for free and then follow the steps in the above link to create your own API key. The only reason why I did not consider my TMDb as sensitive information is because I made it for free and did not attach my credit card or any personal information to their website.

Additionally, some limitations of this data is that the gross revenue does not account for inflation, so we need to be careful if we use this data to compare different year's highest revenue movies.

## Setting up the Container

Here is the link with my dockerhub account image where you can pull my container
https://hub.docker.com/r/nickkalen/project1
Or to save you time you can put this in the terminal:
docker pull nickkalen/project1

To run the container after pulling it, run this line with the xxxxx/yyyyyy part of the discord
url https://discord.com/api/webhooks/xxxxxxx/yyyyyyyyy as the environmental variable

docker run -ti -e MY_PASS=xxxxxx/yyyyyyy nickkalen/project1

Once it is run, the python script will ask you for a year. If you need help, don't type anything and press enter. If you want to exit the prompt, type exit then press enter.
