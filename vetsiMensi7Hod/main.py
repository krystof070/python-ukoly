a = int(input("Zadejte číslo a: "))
b = int(input("Zadejte číslo b: "))
c = int(input("Zadejte číslo c: "))

if a > b:
    p = a
    a = b
    b = p
if b > c:
    p = b
    b = c
    c = p 
if a > b:
    p = a
    a = b
    b = p   

print(f"{a}, {b}, {c}")

min = a
max = a

if b < min:
    min = b
elif b > max:
    max = b
max = a

if c < min:
    min = c
elif c > max:
    max = c

print(f"Největší číslo je {max}.")
print(f"Nejmenší číslo je {min}.")