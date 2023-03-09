import time
print("""
******************************
      Basic Calculator
******************************
      Opeerations
[1]-addition (+)
[2]-substraction (-)
[3]-multiplication (*)
[4]-division (/)
""")
time.sleep(1)
while True:
    a = int(input("First Number: "))
    time.sleep(1)
    b = int(input("Second Number: "))
    time.sleep(1)
    c = int(input("Select Operation: "))
    time.sleep(1)
    if c==1:
        print("First Number: {} \nSecond Nuber: {} \nOperation: Addition (+) \nResult: {}".format(a,b,a+b))
    elif c==2:
        if a>=b:
            print("First Number: {} \nSecond Nuber: {} \nOperation: Substraction (-)  \nResult: {}".format(a,b,a-b))
        else:
            print("The first number sholud not be greater than the second number for positive result!!!")
    elif c ==3:
        print("First Number: {} \nSecond Nuber: {} \nOperation: Multiplication (*) \nResult: {}".format(a,b,a*b))
    elif c==4:
        print("First Number: {} \nSecond Nuber: {} \nOperation: Division (/) \nResult: {}".format(a,b,a/b))
    else:
        print("Invalid operation!!!")