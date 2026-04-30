print("Range Counter")
start = int(input("Enter start: "))
end = int(input("Enter end: "))
even = 0
odd = 0
sum_total = 0
while start <= end:
sum_total = sum_total + start
if start % 2 == 0:
even = even + 1
else:
odd = odd + 1
start = start + 1
print("Even count:", even)
print("Odd count:", odd)
print("Sum:", sum_total)
if even > odd
print("More even numbers")
else:
print("More odd numbers")
