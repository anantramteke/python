s1=input("Enter any string: ")
s2=""
l=len(s1)
if(l<3):
    print(s1)
elif(s1.endswith('ing')):
    s2 = s1 +'ly'
else:
    s2 = s1 + 'ing'
print(s2)
