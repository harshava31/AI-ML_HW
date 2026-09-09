#Section 1: Variables & Data Types

name="Harsha"
age=25
GPA=3.56

print(f"My name is {name} I am {age} years old, GPA is {GPA}")


#Section 2: Input / Output

# Take a number as input from the user and print:Its square its cube
num=int(input("Enter the number:"))
Sq=num**2
cu=num**3
print("Output:")
print("Square:{}".format(Sq))
print("Cube:{}".format(cu))

# Section 3: If-Else  odd_even
if (num%2)==0:
    print("number is even")
else:
    print("number is odd")


#Section 4: Loops
for i in range(num+1):
    print(i)


#Section 5: Functions

def remainder(n):
    rem=n%2
    return rem

print("Remainder:", remainder(num))