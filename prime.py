import math

def isPrime(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    limit = int(math.sqrt(num)) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
            
    return True
