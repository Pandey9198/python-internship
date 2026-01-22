def check(ab):
    def abc():
        print("hello")
        ab()
        print("pandey")
        
    return abc
@check
def hell():
    print("Abhishek")
    
hell()
