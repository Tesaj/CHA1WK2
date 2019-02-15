y=2019
print("Enter your year of birth")
x=input(int)
z=y-x
if z<18:
    print("Minor")
elif z>=18 and z<=38:
    print("Youth")
else:
    print("Elder")