def multiply(num1, num2=2):
    return num1*num2


print(multiply(4, 8))
print(multiply(3.7, 4.2))
print(multiply(5))
print(multiply("dog"))


def sum(*nums):
    total = 0
    for i in nums:
        total += i
    return total


print(sum)


def sigma(funct, *nums):
    total = 0
    for i in nums:
        total += funct(i)
    return total

def square(num):
    return num*num


print(sigma(square, 1,2,3,4,5))
print(sigma(square, *range(1, 6)))

#recursion

def recsum(*nums):
    print("calling recsum on {}".format(nums))
    if len(nums) == 0:
        print("Returning 0")
        return 0
    if len(nums) == 1:
        print("Returning {}".format(nums[0]))
        return nums[0]
    tempsum = recsum(*nums[1:])
    print("Returning {}".format(nums[0] + tempsum))
    return nums[0] + tempsum


print(recsum(1,2,3,4,5))





