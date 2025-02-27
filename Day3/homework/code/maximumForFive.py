def max_for_five(a,b,c,d,e):
    maximum = a
    if maximum < b:
        maximum = b
    if maximum < c:
        maximum = c
    if maximum < d:
        maximum = d
    if maximum < e:
        maximum = e
    return maximum

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
num4 = int(input("enter fiveth number: "))
num5 = int(input("enter sixth number: "))

print(max_for_five(num1,num2,num3,num4,num5))
