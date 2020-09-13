def summation(n):
    if n == 0:
        return n
    return n + summation(n - 1)


a = int(input('Enter a Number: '))
print('Summation is: ' + str(summation(a)))

'''
Explanation:
 
here if a=5 then function summation is called.

so, summation(5) is called.

now n=5 which is not equal to 0.

so, 5+summation(4) is returned, then
        4+summation(3) is returned, then
            3+summation(2) is returned, then
                2+summation(1) is returned, then
                    1+summation(0) is returned, then
                        now as n==0, it will return n which is 0,
                        
so the sequence is = 5+summation(4) = 5+4+summation(3) = 5+4+3+summation(2) = 5+4+3++2+summation(1) = 5+4+3+2+1+summation(0)
= 5+4+3+2+1+0 = 15.
        


'''
