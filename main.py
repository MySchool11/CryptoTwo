__author__ = "Mr Bancroft"

from primitives import calculate_prime_primitives                           # imports the function "primitives" which chooses a prime primitive for the "shared_base"
from prime import get_primes                                                # imports the function "prime" which chooses a random prime from a list up to the passed value
from random import randint                                                  # imports the function "randint" to choose random numbers for alice and bob's secrets

shared_prime = get_primes(1000)                                             # retrieves a random prime between 2 and 1000 and place is into "shared_prime"
shared_base = calculate_prime_primitives(shared_prime)                      # retrieves a random prime primitive of the "shared_prime"

alice_secret = randint(1, 1000)                                             # sets "alice_secret" to a pseudo-random number between 1 and 1000
bob_secret = randint(1, 1000)                                               # sets "bob_secret" to a pseudo-random number between 1 and 1000

print ("\nPublicly shared variables:\n")
print ("Alice and Bob agree upon these two publicly known variables to begin with")
print ("Publicly shared symmetric key: ", shared_prime, " (symmetric because it is the same for both Alice and Bob)")
print ("The symmetric key is always a prime number")
print ("Publicly shared Base: ", shared_base)
print ("The base is always a primitive root of the symmetric key")

print ("\nAlice and Bob now both choose a private number which is totally secret")

alice_send = (shared_base ** alice_secret) % shared_prime                   # calculate the value that alice will send to bob
print ("\nAlice sends over the public channel (Internet): ", alice_send)
print ("which is calculated using her secret number, the shared base and the shared key")

bob_send = (shared_base ** bob_secret) % shared_prime                       # calculate the value that bob will send to alice
print ("Bob sends over the public channel (Internet): ", bob_send)
print ("which is calculated using his secret number, the shared base and the shared key")

print ("\nThis is where the term \"asymmetric\" comes from, as both transmissions are different")

print ("\nPrivately calculated shared secret:")
print ("Now, Alice uses her secret, the number Bob just sent her and the public key to create another number")
alice_shared_secret = (bob_send ** alice_secret) %  shared_prime            # output alice's shard secret
print ("Alice shared secret: ", alice_shared_secret)
print ("Bob does the same but with the number Alice sent him")
bob_shared_secret = (alice_send ** bob_secret) % shared_prime               # output bob's shared secret
print ("Bob shared secret: ", bob_shared_secret)

print ("\nAll being well, both Alice and Bob now have the same shared secret which can be used")
print ("to decrypt the data in combination with their own keys and the public key")

if alice_shared_secret == bob_shared_secret:                                # check that alice and bob's shared secrets do in fact match
    print("\nThe shared secrets match, communication is encrypted securely")  # if equal, confirm  all is well
else:                                                                       # if they are unequal, warn user
    print("\nSomething is wrong there is a secret mismatch, communication is not securely encrypted")
    exit(1)                                                                 # give error code upon exit

exit_string = input("\nPress enter to exit...")

exit(0)                                                                     # give no error code upon exit