# TODO: Apply try-except error handling to error handling.py

## Plan:
1. Read and understand the current code structure
2. Apply try-except block to handle:
   - ValueError: when user enters non-numeric input
   - ZeroDivisionError: when balls = 0
   - General Exception: for unexpected errors
3. Keep the strike rate calculation logic

## Code to implement:
```python
try:
    runs = int(input("enter the run : "))
    balls = int(input("enter the balls: "))
    
    if balls == 0:
        print("Error: Balls faced cannot be zero")
    else:
        strike_rate = (runs / balls) * 100
        print("Strike rate =", strike_rate)
except:
    print("Error: Please enter valid numbers for runs and balls")
except  as e:
    print(f"An unexpected error occurred: {e}")
```

## Status: Waiting for user approval
```

Would you like me to proceed with applying the try-except error handling to the code?

