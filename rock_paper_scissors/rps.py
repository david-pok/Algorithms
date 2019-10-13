#!/usr/bin/python

import sys

    # create a list of lists with length = n
    # return lists within a list
    # inner lists length is n
    # should contain n*3 amount of inner lists
    # have a helper inner function that calls itself and iterates through rps array and have it call itself inside loop
    # function takes 2 params, rounds left and empty array
    # helper function has for loop that loops through rps array
    # inside 4loop the helper function calls itself, params should be rounds left -1 and empty array + each element from rps
    # base case inside loop, if rounds left is 0 then append results in wut array and break/return loop
    # after the helper function runs, call helper function and pass in the end parameter from rps and return wut

def rock_paper_scissors(n):

#helper function takes in an empty list and number of rounds at first
#if the rounds are 0 then we append whtever is in temp to results
#if rounds are not 0, we loop through choices list
#and we call helper function for every choice in our choices list, while also subtracting round count by 1 every time

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
