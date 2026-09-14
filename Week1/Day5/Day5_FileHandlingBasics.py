filename = "sample.txt"

# 1. Write operation
with open(filename, "w") as file:
    file.write("Hello! This is the initial line written to the file.\n")
print(f"Successfully created and wrote to '{filename}'.")

# 2. Append operation
with open(filename, "a") as file:
    file.write("This line was appended later.\n")
print(f"Appended additional text to '{filename}'.")

# 3. Read operation
print(f"\n--- Reading contents of '{filename}' ---")
try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")