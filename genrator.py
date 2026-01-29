# def genrator():
#     for i in range(50):
#         yield i
        
# push=genrator()
# print(next(push))
# print(next(push))
# print(next(push))
# for j in push:
#     print(j)

# def genrator(n):
#     for i in range(n):
#         yield i

def genrate():
    for x in range (20):
        yield x*x
g=genrate()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
