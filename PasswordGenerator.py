import random
import string
print("Choose what type of password you want to generate")
print("Enter 1 for Numeric Password")
print("Enter 2 for Alphabetic Password")
print("Enter 3 for Numeric or Alphabetic or Punchuators Password")
choice=int(input("Enter your choice: "))
if choice==1:
    def password(length):
        password = ""
        for i in range(length):
            password += random.choice('0123456789')
        print(password)
    length=int(input("Enter lenght of password: "))
    print("Generated Password is: ",password(length))
elif choice==2:
    def password(length):
        password = ""
        for i in range(length):
            password += random.choice(string.ascii_letters)
        return(password)
    length=int(input("Enter lenght of password: "))
    print("Generated Password is: ",password(length))
elif choice==3:
    def password(length):
        password = ""
        for i in range(length):
            password += random.choice(string.printable)
        return(password)
    length=int(input("Enter lenght of password: "))
    print("Generated Password is: ",password(length))
else:
    print("Enter Valid Choice")
    
    
    
