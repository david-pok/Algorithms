#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #find each keys value
  #find the modulous thing of each pair
  #take those values and workout how many batches we can make
  batches = []
  for i in ingredients.keys():
    print("INGRED",i)
    for j in recipe.keys():
      print("RECIPE",j)
      if i = j:
        batches.append(i)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))