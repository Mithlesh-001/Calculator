import math  # Imported math module
import numpy # type: ignore # Imported numpy module

# Created a Class of Name Calculator
class Calculator:
	def __init__(self, num1, operator, num2): # Constructor of class Calculator
		self.num1 = num1
		self.operator = operator
		self.num2 = num2

	# Created Function inside the class of name Addition
	def Addition(self):
		return f"The Sum of {self.num1} + {self.num2} = {self.num1 + self.num2}"

	# Created Function inside the class of name Subtraction
	def Subtraction(self):
		return f"The Difference between  {self.num1} - {self.num2} = {self.num1 - self.num2}"

	# Created Function inside the class of name Multiplication
	def Multiplication(self):
		return f"The Product of {self.num1} x {self.num2} = {self.num1 * self.num2}"

	# Created Function inside the class of name Division
	def Division(self):
		return f"the Quotient of {self.num1} ÷ {self.num2} = {self.num1 / self.num2}"

	# Created Function inside the class of name Square
	def square(self):
		return f"The Square of {self.num1} = {self.num1 * self.num1}"

	# Created Function inside the class of name Squareroot
	def squareroot(self):
		return f"The Square Root of {self.num1} = {math.sqrt(self.num1)}"

	def cube(self):
		return f"The Cube of {self.num1} = {self.num1 *self.num1 * self.num1}"

	def cuberoot(self):
		return f"The Cube root of {self.num1} = {numpy.cbrt(self.num1)}"

	def avg(self):
		add = self.num1 + self.num2
		return f"The average of {self.num1} and {self.num2} = {add / 2}"

	def factorial(self):
		return f"The Factorial of {self.num1} = {math.factorial(self.num1)}"


num1 = int(input("Enter the First Number: "))
print('''
	  1. Enter '+' for Addition
	  2. Enter '-' for Subtraction
	  3. Enter '*' for Multiplication
	  4. Enter '/' for Division
	  5. Enter '**' for Square
	  6. Enter '//' for Square root
	  7. Enter '***' for Cube
	  8. Enter '///' for Cube Root
	  9. Type 'Average' for Average
	  10. Type 'factorial' for Factorial
	  ''')
operator = input("Enter the Arithmetic Operator: ")
Cal = Calculator(num1, operator, None)

if operator == '**':
	print(Cal.square())
	exit()
elif operator == "//":
	print(Cal.squareroot())
	exit()
elif operator == '***':
	print(Cal.cube())
	exit()
elif operator == '///':
	print(Cal.cuberoot())
	exit()
elif operator == 'factorial':
	print(Cal.factorial())
	exit()
else:
	num2 = int(input("Enter the Second Number: "))
	cal = Calculator(num1, operator, num2)
	if operator == '+':
		print(cal.Addition())
	elif operator == '-':
		print(cal.Subtraction())
	elif operator == '*':
		print(cal.Multiplication())
	elif operator == '/':
		print(cal.Division())
	elif operator == 'average':
		print(cal.avg())