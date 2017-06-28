__author__ = "Mr Bancroft"

from random import sample

def calculate_prime_primitives(prime):
    number_to_check = 0
    print("Working out public key and public shared base...")                   # displays a message to the user as this process can take some time
    primitive_roots = []                                                        # declares a list "primitive_roots"
    for each in range(1, prime):                                                # loops from 1 until the "prime" value passed into the function
        number_to_check += 1                                                    # adds one to the "number_to_check" variable
        candidate_prime_roots = []                                              # declares a list "candidate_prime_roots"
        for i in range(1, prime):                                               # loops from 1 until the "prime" value passed into the function storing each iteration count in "i"
            modulus = (number_to_check ** i) % prime                            # declares a variable "modulus" and fills it with "number_to_check" to the power "i" modulus the "prime"
            candidate_prime_roots.append(modulus)                               # adds the calculated "modulus" to the "candidate_prime_roots" list
            cleaned_up_candidate_prime_roots = set(candidate_prime_roots)       # uses the "set" method to remove duplicates as only non-repeated numbers will pass into "cleaned_up_candidate_prime_roots"
            if len(cleaned_up_candidate_prime_roots) == len(range(1, prime)):   # if the number of list items in "cleaned_up_candidate_prime_roots" is the same as the number of items between 1
                                                                                # and the prime, then "number_to_check" is a primitive root and so is added to the "primitive_roots" list
                primitive_roots.append(number_to_check)                         # add the confirmed primitive root to the "primitive_roots" list

    return sample(primitive_roots, 1)[0]                                        # return one random primitive root from the "primitive_roots" list