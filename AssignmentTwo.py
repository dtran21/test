endrange= int(input("Enter the value you want your Fibonacci Sequence to end"))
value1 = 0
value2 = 1

for i in range(0,endrange):
    print(value1)
    value1,value2 = value2, value1 + value2