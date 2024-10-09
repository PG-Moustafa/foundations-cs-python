def checkIPv4(ip):
    numbers = ip.split('.')

    if len(numbers) != 4:
        return False

    for n in numbers:
        
        if not n.isdigit():
            return False

        if n != '0' and n.startswith('0'): #0 #012
            return False

        if not (0 <= int(n) <= 255):
            return False
        
    return True

x = input("Enter an IPv4: ")
print(checkIPv4(x))