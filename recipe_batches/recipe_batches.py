#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []

  if len(ingredients) != len(recipe):
    return 0
  else:
    for i in ingredients.keys():
      for j in recipe.keys():
          if i == j:
            batches.append(ingredients[i]//recipe[j])
  for i in range(len(batches)):
    if batches[i] == 0 or len(batches) == 0:
      return 0
    return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))