def squares(n):
    for i in range(1,n+1):
        yield i*i

# squares=lambda n:(i**2 for i in range(1, n+1))   -ламбда израз който връща генератор експрешън

print(list(squares(5)))
