#this block of code is to choose your operator.
while True: 
		op = input("Choose between +|*|-|% or e to end:  ")
		if op == '-' or op == '+' or op == '*' or op == '%':
			break
		elif op == 'e':
			exit()
		else:
			print("please choose one of the following")
#----------------------------------------------------------

#This block of code is where you choose the first number you want to calculate.
while True: 
	try:
		first_number = int(input("Enter the first number or e to end: "))
		break
	except:
		first_number = input("do you want to end? y/n:")
		if first_number == 'y':
			exit()
		elif first_number == 'n':
			print("input needs to be a number")
			continue
		else:
			print("wrong input automaticly does not close script")
			continue
#---------------------------------------------------------------------------

#This block of code is where you choose the second number you want to calculate.
while True: 
	try:
		second_number = int(input("Enter the second number or e to end: "))
		break
	except:
		first_number = input("do you want to end? y/n:")
		if second_number == 'y':
			exit()
		elif second_number == 'n':
			print("input needs to be a number")
			continue
		else:
			print("wrong input automaticly does not close script")
			continue
#---------------------------------------------------------------------------

# giving the answer depending on which one you choose
if op == '*':
	print(first_number * second_number)
elif op == '+':
	print(first_number + second_number)
elif op == '-':
	print(first_number - second_number)
elif op == '%':
	print(first_number % second_number)
#--------------------------------------------------