# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

from num2words import num2words  
 
def function():
    result = 0
    for i in range(1,1001):
        result += (len(''.join(''.join(num2words(i).split('-')).split(' '))))
    return result 

print(function())
