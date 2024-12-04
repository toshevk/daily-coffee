import requests
from random import randint


def retrieve_photo():
     url = "https://coffee.alexflipnote.dev/random"

     response = requests.get(url)
     data = response.content

     with open("static\img.jpg", "wb") as file:
          file.write(data)

def retrieve_quote():
     url = "https://raw.githubusercontent.com/filiphuhta/coffee-quote/refs/heads/main/data/quotes.json"

     response = requests.get(url)
     data = response.json()
     index = randint(0, len(data))

     return data[index]['quote']
