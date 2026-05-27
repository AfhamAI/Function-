def biggest(a, b ,c):
    if a == b == c:
        return "All numbers are equal"
    elif a > b and a > c:
        return f"the largest number is {a}"
    elif b > a and b > c:
        return f"the largest number is {b}"
    elif c > b and c > a:
        return f"the largest number is {c}"
    else:
        return "Invalid"


x = int(input("Enter yours 1st number"))
y = int(input("Enter yours 2nd number"))
z = int(input("Enter yours 3rd number"))

print(biggest(x, y , z))
