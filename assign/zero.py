a=3
try:
    if a<4:
        b=a/(a-3)
        print(b)
except(ZeroDivisionError):
    print("divisor is zero")
    
