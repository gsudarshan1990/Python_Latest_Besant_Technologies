x="Hello World"
print(type(x))

x=20
print(type(x))

x=20.5
print(type(x))

x=1j
print(type(x))

x=["Raj","Durga","Keerthana"]
print(type(x))

x=("apple","banana","cherry")
print(type(x))

x=range(6)
print(type(x))

x={"name":"John","age":18}
print(type(x))

x=True
print(type(x))


def multiply():
    numstr1=input('Enter the number1:')
    numstr2=input('Enter the number2:')
    num1float=float(numstr1)
    num2float=float(numstr2)
    print('The product of two numbers',num1float*num2float)

multiply()



