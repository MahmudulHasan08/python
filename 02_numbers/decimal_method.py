# from decimal import Decimal

print(0.2 + 0.3 + 0.4)

# when below this code we run in command shell then result is 
# unpredictable so then we use decimal for this correct solution then code would be 

from decimal import Decimal

print(Decimal('0.2') + Decimal('0.3') + Decimal('0.4'))