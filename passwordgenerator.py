import random

complexity = input("How complex of a password would you like? (1 - 3)>")

complexity = int(complexity)

if complexity == 1:
    print(range(0, 999999))
elif complexity == 2:
    print(hex(int(random.randint(0, 99999999))))
elif complexity == 3:
    randthing = [",", "%", "}", "46", "@", "a", "b", "c"]
    password = []
    for _ in range(20):
        password.append(random.choice(randthing))
    print(password)