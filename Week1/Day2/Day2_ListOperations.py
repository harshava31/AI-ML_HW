numbers = [25, 10, 5, 40]
print(f"Initial list:       {numbers}")

numbers.append(30)
print(f"After append(30):   {numbers}")

numbers.insert(2, 15)
print(f"After insert(2, 15):{numbers}")

numbers.remove(10)
print(f"After remove(10):   {numbers}")

numbers.sort()
print(f"After sort():       {numbers}")

numbers.reverse()
print(f"After reverse():    {numbers}")