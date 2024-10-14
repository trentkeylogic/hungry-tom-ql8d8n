#!/bin/env python3

import httpx
import json
import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index_root():
  return potion_page

with open('index.html', 'r') as file:
  potion_page=file.read()


#if __name__ == "__main__":
#  app.run()

r = httpx.get('https://api.potterdb.com/v1/potions')
potions=json.loads(r.text)['data']
#print(r.status_code)
#print(r.headers['content-type'])
potion=potions[random.randrange(len(potions))]['attributes']
print(potion['image'])
print(potion['name'])
print(potion['effect'])
print(potion['ingredients'])
