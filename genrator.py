def genrator():
    for i in range(50):
        yield i
        
push=genrator()
print(next(push))
print(next(push))
print(next(push))
# for j in push:
#     print(j)

# def genrator(n):
#     for i in range(n):
#         yield i
        
print(list(genrator(10)))
print(tuple(genrator(10)))
print(set(genrator(10)))