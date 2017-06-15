__author__ = "Mr Bancroft"

from random import sample

# a simple function to find all the prime numbers in a given range (determined by the
# max_number_to_find_primes_to variable in main.py

def get_primes(range_max):
    number_range = set(range(range_max,1,-1))                                   # "set()" declares an unordered collection with
                                                                                # no duplicates. "range()" creates a range of numbers
                                                                                # starting at the passed in value n and ending at the item at index 1, counting back 1 every step so if 10
                                                                                # were passed it would create 2,3,4,5,6,7,8,9,10, this unordered collection of numbers is put into "number_range"
    primes = []                                                                 # declares an array "primes"
    while number_range:                                                         # while loop that works through the range "number_range"
        p = number_range.pop()                                                  # creates a variable "p" and places the first value in "numbers" into is using "pop()"
        primes.append(p)                                                        # adds (appends) "p" to the "primes" array
        number_range.difference_update(set(range(p * 2, range_max + 1, p)))     # uses "difference_update" to remove the non prime numbers from the array "number_range"
    return sample(primes, 1)[0]                                                 # returns the array a random value from [primes]