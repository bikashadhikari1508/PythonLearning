from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True
    
def prime_for_a_given_range(start,end):
    return [num for num in range(start,end+1) if is_prime(num)]

start = int(input('Enter 1st num: '))
end = int(input("Enter 2nd num "))

res = prime_for_a_given_range(start,end)
print("prime numbers in the given range: ", res)