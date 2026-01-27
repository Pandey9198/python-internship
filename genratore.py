def genrator():
    for i in range(50):
        yield i
        
push=genrator()
# print(next(push))
# print(next(push))
# print(next(push))
for j in push:
    print(j)