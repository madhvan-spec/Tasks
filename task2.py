# Calculating Factorial using recursion
def calc_fact(nbr):
    ans = 1
    if nbr >=1:
        return nbr * calc_fact(nbr-1)
        
    else:
        return 1
    
try:
    nbr = int(input("Please Enter the Number: "))
    ans = calc_fact(nbr)
    print(f" {nbr}! = {ans}")
except Exception as e:
    print("Please Enter a Valid Number")