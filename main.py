count = int(input("Enter the count of integers: "))
product = 1
for i in range(count):
    x = int(input("Enter the integer: "))
    product = round(product * x)
print("The product of the provided integers is ",product)