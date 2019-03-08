'''
Euclidean Algorithm:
The Euclidean algorithm is a way to find the greatest common divisor of two positive integers
Example:
This is based on simple algorithms based on Euclidean algorithms where gcd of 96 and 60 can be figure out in this way:
    96=60.1+36
    60=36.1+24
    36=24.1+12 
    24=12.2+0 => Here is the zero so. previous reminder is 12 hence the gcd of 96 and 60 is 12
'''

def gcd(a, b):
    while(b !=0):
        t=a
        a=b
        b=t%b
    return a
# Try out the function with few examples
print(gcd(96,60)) # should be 12
print(gcd(10,13)) # should be 1
print(gcd(1701,3768)) # should be 3