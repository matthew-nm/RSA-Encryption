def prime_test(num):
    
    # Test simple cases
    if num == 2 or num == 3:
        return True
    elif int(num)!=num or num<=1 or num%2==0:
        return False
        
    # Test all possible odd factors
    for x in range(3, int(sqrt(num))+1, 2):
        if num % x == 0:
            return False

    return True