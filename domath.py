from __future__ import print_function
try:
	input = raw_input
except:
	pass

num1 = int(input("Enter integer 1 :"))
num2 = int(input("Enter integer 2 :"))

print ("Addition:", num1, " + ", num2, " = ", num1+num2)
print ("Multiplication:", num1, " * ", num2, " = ", num1*num2)
q = float(num1)/num2
print ("division:", float(num1), " / ", num2, " = ", "%06.2f" % q)