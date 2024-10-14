#!/bin/env python3

import httpx
import json
import random
from flask import Flask

app = Flask(__name__)

potions=json.loads(httpx.get('https://api.potterdb.com/v1/potions').text)['data']

with open('index.html', 'r') as file:
  potion_page=file.read()
  file.close()

@app.route("/")
def index_root():
  #with open('index.html', 'r') as file:
  #  potion_page=file.read()
  #  file.close()

  potion=potions[random.randrange(len(potions))]['attributes']
  return potion_page.replace('potion_name', str(potion['name'])).replace('potion_image', str(potion['image'])).replace('potion_effect', str(potion['effect'])).replace('potion_ingredients', str(potion['ingredients']))

if __name__ == "__main__":
  app.run()

exit()

print(potion['image'])
print(potion['name'])
print(potion['effect'])
print(potion['ingredients'])
