# To Check if a number is prime 
def check_prime(nbr):
    for i in range(2,nbr//2):
        if(nbr % i == 0):
            return False
        else:
            return True
    
try:
    nbr = int(input("Please Enter a Number: "))
    result_string = "Prime" if check_prime(nbr) else "Not Prime"
    print(f"Number {nbr} is {result_string}")
except Exception as e:
    print("Please Enter a Valid Number")

