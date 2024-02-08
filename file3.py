s1 = input("Enter Your Name: ")
L = s1.split()
ch = [part[0].upper() for part in s1.split()]
#print(ch)
print(''.join(ch))

