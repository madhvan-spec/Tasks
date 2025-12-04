def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except TypeError:
        return "Both inputs must be numbers."
    else:
        return f"Result: {result}"


print(divide(265, 34))   
print(divide(788, 0))    
print(divide("M", 3))  
