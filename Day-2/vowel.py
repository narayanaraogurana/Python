#wWrite a program for volwel or not
a=input("enter a string")
if len(a)==1:
    if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
        print("vowel")
    else:
        print("Constant")
else:
    print("Please enter a single character")