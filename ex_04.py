def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))   # 5
print(fibonacci(10))  # 55
print(fibonacci(12))  # 144