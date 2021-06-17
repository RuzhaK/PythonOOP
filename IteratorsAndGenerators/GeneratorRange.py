def genrange(start,end):
    while start<=end:
        yield start
        start+=1

# genrange = lambda start, end: (i for in in range(start,end+1))  - втори вариант с генератор експрешън;range самия си връща генератор;

print(list(genrange(1, 10)))