# Public Values
P = 23
G = 9

print("Public Prime Number P =", P)
print("Public Primitive Root G =", G)

# Alice Private Key
alice_private = 4

# Bob Private Key
bob_private = 3

# Alice Public Key
alice_public = (G ** alice_private) % P
print("Alice Public Key =", alice_public)

# Bob Public Key
bob_public = (G ** bob_private) % P
print("Bob Public Key =", bob_public)

# Shared Secret Key
alice_secret = (bob_public ** alice_private) % P
bob_secret = (alice_public ** bob_private) % P

print("Alice Secret Key =", alice_secret)
print("Bob Secret Key =", bob_secret)