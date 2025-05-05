































import math

def num_divisors(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors += 2  
            if i == n // i:  
                divisors -= 1  
    return divisors

def find_triangle_with_divisors(limit):
    n = 1
    while True:
        triangle = n * (n + 1) // 2
        
        # Beräkna delarna för n och n+1
        if n % 2 == 0:
            divisors_n = num_divisors(n // 2)  
            divisors_n_plus_1 = num_divisors(n + 1)
        else:
            divisors_n = num_divisors(n)
            divisors_n_plus_1 = num_divisors((n + 1) // 2)  

        total_divisors = divisors_n * divisors_n_plus_1
        
        # Om delarna är större än limit, returnera triangeltalet
        if total_divisors > limit:
            return triangle
        
        n += 1  # Gå vidare till nästa n

result = find_triangle_with_divisors(500)
print("Det första triangeltalet med fler än 500 delare är:", result)