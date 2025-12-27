print("start")
print("Executing Handling With Specific Error Type:")
try:
    print(15/0)
except ZeroDivisionError:
    print("we can't the value with zero")
print("stop")