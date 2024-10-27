N = int(input("Please enter a positive integer N: "))
numbers = []

for i in range(N):
    num = int(input(f"Please enter number {i + 1}: "))
    numbers.append(num)

X = int(input("Please enter the integer X to find: "))

if X in numbers:
    index = numbers.index(X) + 1
    print(f"The index of {X} is: {index}")
else:
    print("-1")
