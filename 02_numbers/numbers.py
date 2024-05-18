import math

x = 2
y = 3
z = 4
#  its a bad practise 
result = x + y * z
# its good practice for developer always calcultaing anything 
# that time each calculating section should be each part separate to pranthesis or brackets etc.
result = x + ( y * z )

a = 10
b = 12.5
c = 15

result1 = a + b
# good practice below this code because of references was float type so
# converted it to int type for better practice 
result2 = a + int(b)
result3 = float(a) + b
result4 = a ** 100
result5 = a + int(b), c * 2
print(result5)
print(b.__floor__)