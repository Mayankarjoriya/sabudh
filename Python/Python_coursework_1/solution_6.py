"""Write a program to reverse given numbers without slicing. Input will be a positive integer."""
n = int(input("enter a number: "))

r_n = 0

while n > 0:
    digit = n % 10
    r_n = r_n * 10 + digit
    n = n // 10

print(r_n)