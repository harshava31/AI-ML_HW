def nodd(num):
   if (num%2)==0:
    print("{} is even".format(num))
   else:
    print("{} is odd".format(num))

# Reads input string -> splits into list of strings -> converts each to integer
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Your list:", numbers)
# Input:  10 20 30 40

for i in numbers:
  nodd(i)

  

