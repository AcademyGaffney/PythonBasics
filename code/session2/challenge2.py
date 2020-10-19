x = input("Number 1: ")
y = input("Number 2: ")

x = float(x)
y = float(y)

output = "{:.2f} {} {:.2f} = {:.2f}"

print(output.format(x, "**", y, x**y))
print(output.format(x, "*", y, x*y))
print(output.format(x, "/", y, x/y))
print(output.format(x, "//", y, x//y))
print(output.format(x, "%", y, x%y))
print(output.format(x, "+", y, x+y))
print(output.format(x, "-", y, x-y))