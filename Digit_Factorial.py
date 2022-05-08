"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
def factorial(num):
    
    product = num
    for i in range(2, num):
        product *= i
    return product

def check_sum(number):
    list_digits = list(str(number))
    check_sum = 0
    for digit in list_digits:
        check_sum += factorial(int(digit))
    if check_sum == number:
        return True

def find_final_sum():
    
    final_list = []
    final_sum = 0
    counter = 3
    while counter < 200000:
        if check_sum(counter):
            final_list.append(counter)
            counter += 1
        else:
            counter += 1

    for j in final_list:
        final_sum += j
    print(final_sum)

find_final_sum()