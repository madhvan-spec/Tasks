# Function to reverse String
def rev_string(s):
    return s[::-1]

s = input("Please Enter a String: ")
reversed_string = rev_string(s)
print(f"Reverse of {s} is {reversed_string}")