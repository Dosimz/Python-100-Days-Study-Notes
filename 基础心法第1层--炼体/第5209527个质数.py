def is_prime(n):
    count = 0
    prime = []
    for _ in range(n+1):
        prime.append(True)
    for i in range(2, n+1):
        if prime[i]:
            print(i)
            count += 1
            j = i + i
            while j <= n:
                prime[j] = False
                j += i
    print(count)
is_prime(90990000)