for i in range(1, 11):
    for j in range(1, 11):
        print("{:>4}".format(i*j), end="")
    print()

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print("{:>4}".format(i+j), end="")
        j += 1
    print()
    i += 1
