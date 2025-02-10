import requests
from random import randint
from PIL import Image
from io import BytesIO

def retrieve_photo():
     image_url = "https://coffee.alexflipnote.dev/random"
     try:
          response = requests.get(image_url)
          response.raise_for_status()
     except requests.exceptions.RequestException as e:
          return "static/images/img.jpg"

     img = Image.open(BytesIO(response.content))
     if img.mode != "RGB":
          img = img.convert("RGB")

     original_width, original_height = img.size
     desired_height = 512
     aspect_ratio = original_width/original_height
     new_width = int(desired_height * aspect_ratio)
     img = img.resize((new_width, desired_height))

     img.save("static/images/img.jpg")
     return "static/images/img.jpg"

def retrieve_quote():
     url = "https://raw.githubusercontent.com/filiphuhta/coffee-quote/refs/heads/main/data/quotes.json"

     response = requests.get(url)
     data = response.json()
     index = randint(0, len(data) - 1)

     return data[index]['quote']

if __name__ == "__main__":
     retrieve_photo()
     retrieve_quote()