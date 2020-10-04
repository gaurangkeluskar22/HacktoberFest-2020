
def power(a, b, c):
    return (a ** b) % c

p, q = [int(x) for x in input("Enter two prime no separated by space:").split()]
print("Public keys are {} and {}".format(p, q))
r = int(input("Enter private key for Alice:"))
s = int(input("Enter private key for Bob:"))
x = power(p, r, q)
y = power(p, s, q)
print("Now {} and {} is exchanged over a channel" .format(x, y))
key1 = power(y, r, q)
key2 = power(x, s, q)
print("Secret key for Alice:", key1)
print("Secret key for Bob:", key2)
