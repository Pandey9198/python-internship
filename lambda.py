<<<<<<< HEAD
x=5
def fun(x):
    return x +10
print(fun (x))

fun = lambda x: x +10
print(fun(5)) 

print((lambda x: x+10)(5)) # one line lambda
# pultiply numbers throw lambda 
multiply =lambda a,b: a*b
print(multiply (4,3))

fun =lambda: "hello"
print (fun())
=======
# x=5
# def fun(x):
#     return x +10
# print(fun (x))

# fun = lambda x: x +10
# print(fun(5))

# print((lambda x: x+10)(5)) # one line lambda
# # pultiply numbers throw lambda
# multiply =lambda a,b: a*b
# print(multiply (4,3))

# fun =lambda: "hello"
# print (fun())
>>>>>>> c9e4d9ac9e57fb19e93c2ec5071b4c1a76c21390

lst = ["Abhishek","pandey","bhopal","mcu"]

lst = sorted(lst, key=lambda x: len(x))
print(lst)  

