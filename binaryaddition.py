
def binary_to_decimal(bn):
    temp = bn
    decimal_nbr = 0
    i = 0
    while temp > 0:
        last_digit = temp % 10
        decimal_nbr = decimal_nbr + last_digit * (2**i)
        i = i + 1
        temp = temp // 10
    return decimal_nbr

def decimal_to_binary(dn):
    if dn == 0:
        return 0
    
    bits = []
    while dn > 0:
        remainder = dn % 2
        bits.append(str(remainder))
        dn = dn // 2

    return ''.join(bits[::-1])


bn1 = int(input("Enter First Binary Number: "))
bn2 = int(input("Enter Second Binary Number: "))
dn1 = binary_to_decimal(bn1)
dn2 = binary_to_decimal(bn2)
ans = dn1 + dn2
print(f"Addition of Binary Numbers {bn1} and {bn2} is {ans}")

temp1 = decimal_to_binary(dn1)
print(temp1)