"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(n):
    list = []
    if(n <=0):
        raise ValueError("Please enter a valid argument which is equal or bigger than one")
    # check up to square root n
    list_size = 0
    start = 2
    is_prime = True
    while (list_size< n):
        # check is prime
        #for i in range(2,int(start**(1/2))): // failed on 4
        for i in range(2, start):
            if start% i== 0:
                is_prime = False
                break

        if is_prime:
            list.append(start)
            list_size+=1
        # reinitizaliz3
        start+=1
        is_prime = True

    # for i in range(1,n):
    #     is_prime = True
    #     for j in range(1,int(i**(1/2))):
    #         if i % j ==0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         list.append(i)   

    return list
