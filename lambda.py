
def fun(x):
    return x +10
print(fun (5))

fun = lambda x: x +10
print(fun(5))

print((lambda x: x+10)(5)) # one line lambda
# pultiply numbers throw lambda 
multiply =lambda a,b: a*b
print(multiply (4,3))

fun =lambda: "hello"
print (fun())

lst = ["Abhishek","pandey","bhopal","mcu"]

lst = sorted(lst, key=lambda x: len(x))
print(lst)  
