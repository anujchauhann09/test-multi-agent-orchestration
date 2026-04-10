def isPrime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return True
        
    return False