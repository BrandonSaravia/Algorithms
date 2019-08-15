#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  for x in recipe:
    if x not in ingredients:
      batches = 0
      return batches
    elif ingredients[x] - recipe[x] < 0:
      batches = 0
      return batches
    elif ingredients[x] / recipe[x] >= 0:
      if x == list(recipe)[0]:
        batches = int(ingredients[x] / recipe[x])
      elif int(ingredients[x] / recipe[x]) <= batches:
        batches = int(ingredients[x] / recipe[x])
  return batches

# recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
# ingredients = { 'milk': 1032, 'butter': 1000, 'flour': 51 }

# print(recipe_batches(recipe, ingredients))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))