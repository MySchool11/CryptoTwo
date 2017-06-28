__author__ = "Mr Bancroft"

# PLEASE do not be put off by the apparent complexity of this code, you do not need to understand how it works, just
# this information it is giving you when you run it!!!

from primitives import calculate_prime_primitives  # imports the function "primitives" which chooses a prime primitive for the "shared_base"
from prime import get_primes  # imports the function "prime" which chooses a random prime from a list up to the passed value
from random import randint  # imports the function "randint" to choose random numbers for alice and bob's secrets
from textwrap import wrap  # imports the function "wrap" to help format the huge numbers in a readable fashion
from time import sleep  # imports the function "sleep" to allow pauses in the program
from sys import stdout  # imports the namespace "stdout" from which the "write" function is used for writing multiple things to one line


def print_arrows(output_string): # function to print symbols in increasing amounts one after the other every second for five seconds, provides some very basic animation
    s = ""
    for i in range(0, 5):
        s += output_string
        stdout.write(s)
        stdout.flush()
        sleep(1)
    print("\n")


pause_time = 7  # sets the number of seconds for each pause to read the text
internet_transfer_animation = "---->" # sets the string used for the Internet transfer 'animation'
calculating_equal_shared = "*-*" # sets the string used for the shared secret comparison 'animation'

print("Diffie-Hellman encryption\n")

shared_prime = get_primes(1000)  # retrieves a random prime between 2 and 1000 and place is into "shared_prime"
shared_base = calculate_prime_primitives(shared_prime)  # retrieves a random prime primitive of the "shared_prime"

alice_secret = randint(1, 1000)  # sets "alice_secret" to a pseudo-random number between 1 and 1000
bob_secret = randint(1, 1000)  # sets "bob_secret" to a pseudo-random number between 1 and 1000

print("\nwe start with two publicly shared variables:\n")
print("Alice and Bob agree upon these two variables to begin with\n")
print("1) a publicly shared symmetric key: ", shared_prime,
      " (symmetric because it is the same for both Alice and Bob)")
print("   the symmetric key is always a prime number")
print("2) a publicly shared Base: ", shared_base)
print("   the base is always a primitive root of the public key")

next_bit = input("\nPress enter to continue...")

print("\nAlice and Bob now both choose a private number which is totally secret")
print("this number can be any number and does not have to be a prime or other special number")

sleep(pause_time)

alice_send = (shared_base ** alice_secret) % shared_prime  # calculate the value that alice will send to bob
print("\nAlice sends over the public channel (Internet): ", alice_send)
print("which is calculated using her secret number, the shared base and the shared key\n")

sleep(pause_time)

print_arrows(internet_transfer_animation)

next_bit = input("\npress enter to continue or press 'a' then enter to see the maths in detail...")
if next_bit == "a":
    print("\nthe number Alice sends is the shared base to the power of her secret number")
    answer = wrap(str(shared_base ** alice_secret), width=100)
    for i in range(len(answer)):
        print(answer[i])
    print("modulo the shared key, " + str(shared_prime) + ", which gives us the number Alice sends to Bob\n")
    next_bit = input("press enter to continue...")

bob_send = (shared_base ** bob_secret) % shared_prime  # calculate the value that bob will send to alice
print("\nBob sends over the public channel (Internet): ", bob_send)
print("which is calculated using his secret number, the shared base and the shared key\n")

sleep(pause_time)

print_arrows(internet_transfer_animation)

next_bit = input("\npress enter to continue or press 'a' then enter to see the maths in detail...")
if next_bit == "a":
    print("\nthe number Bob sends is the shared base to the power of his secret number")
    answer = wrap(str(shared_base ** bob_secret), width=100)
    for i in range(len(answer)):
        print(answer[i])
    print("modulo the shared key, " + str(shared_prime) + ", which gives us the number Bob sends to Alice\n")
    next_bit = input("press enter to continue...")

print("\nThis is where the term \"asymmetric\" comes from, as both transmissions are different\n")

sleep(pause_time - 2)

print("next, both Alice and bob privately calculate the shared secret\n")
print("so, Alice uses her secret with the number Bob just sent her and the public key to create another number")
alice_shared_secret = (bob_send ** alice_secret) % shared_prime  # output alice's shard secret
print("Alice calculate the shared secret to be ", alice_shared_secret)

next_bit = input("\npress enter to continue or press 'a' then enter to see the maths in detail...")
if next_bit == "a":
    print("\nthe number Alice works out as the shared secret is the number Bob sent to the power of her secret")
    answer = wrap(str(bob_send ** alice_secret), width=100)
    for i in range(len(answer)):
        print(answer[i])
    print("modulo the shared key, " + str(shared_prime) + ", which gives us Alice's copy of the shared secret\n")
    next_bit = input("press enter to continue...")

print("\nBob does the same but with the number Alice sent him")
bob_shared_secret = (alice_send ** bob_secret) % shared_prime  # output bob's shared secret
print("Bob calculates the shared secret to be ", bob_shared_secret)

next_bit = input("\npress enter to continue or press 'a' then enter to see the maths in detail...")
if next_bit == "a":
    print("\nthe number Bob works out as the shared secret is the number Alice sent to the power of his secret")
    answer = wrap(str(alice_send ** bob_secret), width=100)
    for i in range(len(answer)):
        print(answer[i])
    print("modulo the shared key, " + str(shared_prime) + ", which gives us the Bob's copy of the shared secret\n")
    next_bit = input("press enter to continue...")

print("\ncheck that Alice's shared secret == Bob's shared secret\n")
print_arrows(calculating_equal_shared)
if alice_shared_secret == bob_shared_secret:  # check that alice and bob's shared secrets do in fact match
    print("\nThe shared secrets match, communication is encrypted securely")  # if equal, confirm  all is well
else:  # if they are unequal, warn user
    print("\nSomething is wrong there is a secret mismatch, communication is not securely encrypted")
    exit(1)

print("\nnow the shared secret can be used to decrypt the message by both Alice and Bob")

exit_string = input("\nPress enter to exit...")  # give error code upon exi

exit(0)  # give no error code upon exit
