num1 = float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
operator= input("Enter the operation (+,-,/,x): ")

if operator == "+":
      print(num1+num2) 
elif operator == "-":
      print(num1-num2) 
elif operator == "/":
      print(num1/num2)
else:
      print(num1*num2)