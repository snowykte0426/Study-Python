num, result = int(input("Enter the number: ")), 1
for i in range(1, num + 1):
    result *= i
print(f"Factorial({num}!):{result}")