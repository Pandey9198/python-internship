# try:
#     user_runs = input("Enter runs scored by Abhishek: ")
#     user_balls = input("Enter balls faced by : ")
    
#     runs = int(user_runs)
#     balls = int(user_balls)
    
#     if balls == 0:
#         print("Error: Balls faced cannot be zero")
#     else:
#         strike_rate = (runs / balls) * 100
#         print(f"Abhishek's strike rate = {strike_rate:.2f}")
#         print("this is important")
# except ValueError:
#     print("Error: Please enter valid numbers for runs and balls")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
    
#    

    
runs = int(input("enter the run : "))
balls = int(input("enter the balls: "))
strike_rate = (runs / balls) * 100
print("Strike rate =", strike_rate)


print ("hello")


